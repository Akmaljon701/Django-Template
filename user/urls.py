from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from user.views import *

urlpatterns = [
    path('token/', CustomUserTokenView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

    path('current/', CurrentCustomUser.as_view()),
    path('create/', CustomUserCreateView.as_view()),
]
