from django.contrib.auth import authenticate
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *


class CustomUserCreateView(APIView):
    @swagger_auto_schema(request_body=CustomUserSerializer)
    def post(self, request):
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


class CurrentCustomUser(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data, status=200)


class CustomUserUpdateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=CustomUserSerializer)
    def put(self, request):
        serializer = CustomUserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Updated successfully!',
                             'user': serializer.data}, status=200)
        return Response({'detail': 'Bad Request!',
                         'data': serializer.errors}, status=400)


class CustomUserDeleteView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        request.user.delete()
        return Response({'detail': 'Deleted successfully!'}, status=200)


