from django.urls import path
from user.views import *

urlpatterns = [
    path('token/', CustomUserTokenView.as_view()),
    path('current/', CurrentCustomUser.as_view()),
    path('create/', CustomUserCreateView.as_view()),
]
