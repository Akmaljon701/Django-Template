from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from user.views import *

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

    path('create/', create_custom_user),
    path('update/', update_custom_user),
    path('delete/', delete_custom_user),
    path('current/', get_current_user),
    path('', get_users),
]
