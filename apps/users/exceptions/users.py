class RequiredUserSigninFieldError(Exception):
    """required user signin field error"""

    def __str__(self):
        return "Required User Signin Field."


class RequiredUserSignupFieldError(Exception):
    """required user signup field error"""

    def __str__(self):
        return "Required User Signup Field."


class InvalidSigninCredentialsError(Exception):
    """invalid signin credential error"""

    def __str__(self):
        return "Invalid Signin Credential."


class NotActiveUserError(Exception):
    """not active user error"""

    def __str__(self):
        return "Is deactivated User."


class NotFoundUserError(Exception):
    """not found user error"""

    def __str__(self):
        return "Not Found User."


class IsDormantUserError(Exception):
    """is dormant user error"""

    def __str__(self):
        return "Is Dormant User."


class IsAlreadyExistUserEmailError(Exception):
    """is already exist user email error"""

    def __str__(self):
        return "Is Already Exist User Email."
