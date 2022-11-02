import base64
import hashlib
import math

from django.utils.crypto import (
    RANDOM_STRING_CHARS,
    constant_time_compare,
    get_random_string,
    pbkdf2,
)


class PBKDF2PasswordHasher:
    algorithm = "pbkdf2_sha256"
    iterations = 260000
    digest = hashlib.sha256
    salt_entropy = 128

    def salt(self):
        char_count = math.ceil(self.salt_entropy / math.log2(len(RANDOM_STRING_CHARS)))
        return get_random_string(char_count, allowed_chars=RANDOM_STRING_CHARS)

    def encode(self, password, salt, iterations=None):
        assert password is not None
        assert salt and "$" not in salt
        iterations = iterations or self.iterations
        hash = pbkdf2(password, salt, iterations, digest=self.digest)
        hash = base64.b64encode(hash).decode("ascii").strip()
        return "%s$%d$%s$%s" % (self.algorithm, iterations, salt, hash)

    def decode(self, encoded):
        algorithm, iterations, salt, hash = encoded.split("$", 3)
        assert algorithm == self.algorithm
        return {
            "algorithm": algorithm,
            "hash": hash,
            "iterations": int(iterations),
            "salt": salt,
        }

    def verify(self, password, encoded):
        decoded = self.decode(encoded)
        encoded_2 = self.encode(password, decoded["salt"], decoded["iterations"])
        return constant_time_compare(encoded, encoded_2)

    def harden_runtime(self, password, encoded):
        decoded = self.decode(encoded)
        extra_iterations = self.iterations - decoded["iterations"]
        if extra_iterations > 0:
            self.encode(password, decoded["salt"], extra_iterations)


def check_password(password, encoded, setter=None) -> bool:
    hasher = PBKDF2PasswordHasher()
    is_correct = hasher.verify(password, encoded)
    if not is_correct:
        hasher.harden_runtime(password, encoded)
    if setter and is_correct:
        setter(password)
    return is_correct


def make_password(password, salt=None) -> str:
    hasher = PBKDF2PasswordHasher()
    salt = salt or hasher.salt()
    return hasher.encode(password, salt)
