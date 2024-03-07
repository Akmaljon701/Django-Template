from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from user.views import *

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

    path('create/', CustomUserCreateView.as_view()),
    path('update/', CustomUserUpdateView.as_view()),
    path('delete/', CustomUserDeleteView.as_view()),
    path('current/', CurrentCustomUser.as_view()),
]
