from django.contrib.auth import authenticate
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from utils.auth_user import check_user
from .serializers import *


@swagger_auto_schema(method='post', request_body=CustomUserSerializer)
@api_view(['POST'])
def create_custom_user(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(is_active=True)
        user = authenticate(username=serializer.validated_data['username'],
                            password=serializer.validated_data['password'])
        refresh = RefreshToken.for_user(user)
        serialized_user = CustomUserSerializer(user).data
        return Response({'detail': 'Created successfully!',
                         'refresh': str(refresh),
                         'access': str(refresh.access_token),
                         'user': serialized_user}, status=201)
    return Response({'detail': 'Bad Request!',
                     'data': serializer.errors}, status=400)


@api_view(['GET'])
def get_current_user(request):
    user = check_user(request)
    serializer = CustomUserSerializer(user)
    return Response(serializer.data, status=200)


@swagger_auto_schema(method='put', request_body=CustomUserSerializer)
@api_view(['PUT'])
def update_custom_user(request):
    user = check_user(request)
    serializer = CustomUserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'detail': 'Updated successfully!',
                         'user': serializer.data}, status=200)
    return Response({'detail': 'Bad Request!',
                     'data': serializer.errors}, status=400)


@api_view(['DELETE'])
def delete_custom_user(request):
    user = check_user(request)
    user.delete()
    return Response({'detail': 'Deleted successfully!'}, status=200)
