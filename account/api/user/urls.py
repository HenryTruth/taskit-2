from django.contrib import admin
from django.urls import path, include

from .views import UserDetailApiView, UserStatusAPIView

app_name = 'user'

urlpatterns = [
    path('<username>/', UserDetailApiView.as_view(), name='detail'),
    path('<username>/todos/', UserStatusAPIView.as_view(), name='detail')
]