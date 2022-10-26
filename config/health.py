from django.http import HttpResponse


class HealthCheck:
    """health check"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == "/hc":
            return HttpResponse("pong")
        response = self.get_response(request)
        return response
