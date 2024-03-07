from rest_framework.exceptions import PermissionDenied
from rest_framework_simplejwt.authentication import JWTAuthentication


def check_user(request):
    auth_result = JWTAuthentication().authenticate(request)
    if auth_result is None:
        raise PermissionDenied('Not authenticated')
    user, jwt_payload = JWTAuthentication().authenticate(request)
    return user
