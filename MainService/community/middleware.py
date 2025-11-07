import jwt
from django.conf import settings
from django.http import JsonResponse
from jwt.exceptions import InvalidTokenError, DecodeError

class JWTAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        actk_header = request.headers.get("Authorization")
        if not actk_header:
            return JsonResponse({"message": "No token provided"}, status=400)
        
        actk = actk_header.split(" ")[1]
        try:
            payload = jwt.decode(actk, settings.SECRET_JWT_KEY, algorithms=["HS256"])
            request.username = payload.get("sub")
        except (InvalidTokenError, DecodeError):
            return JsonResponse({"message": "Token is invalid or expired"}, status=401)
        
        res = self.get_response(request)
        return res