from django.contrib.auth import authenticate
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
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
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def get_current_user(request):
    serializer = CustomUserSerializer(request.user)
    return Response(serializer.data, status=200)


@swagger_auto_schema(method='put', request_body=CustomUserSerializer)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def update_custom_user(request):
    serializer = CustomUserSerializer(request.user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'detail': 'Updated successfully!',
                         'user': serializer.data}, status=200)
    return Response({'detail': 'Bad Request!',
                     'data': serializer.errors}, status=400)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def delete_custom_user(request):
    request.user.delete()
    return Response({'detail': 'Deleted successfully!'}, status=200)
