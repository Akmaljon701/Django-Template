from django.contrib.auth import authenticate
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *


class CustomUserTokenView(APIView):
    @swagger_auto_schema(request_body=CustomUserTokenSerializer)
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            return Response({'detail': 'User not found', 'success': False}, status=404)
        refresh = RefreshToken.for_user(user)
        serialized_user = CustomUserSerializer(user).data
        return Response({'refresh': str(refresh), 'access': str(refresh.access_token), 'user': serialized_user})


class CurrentCustomUser(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data, status=200)


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
                             'success': True,
                             'refresh': str(refresh),
                             'access': str(refresh.access_token),
                             'user': serialized_user}, status=201)
        return Response({'detail': 'Bad Request!',
                         'success': False,
                         'data': serializer.errors}, status=400)




