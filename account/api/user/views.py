from django.contrib.auth import get_user_model
from rest_framework import permissions, generics,pagination
from .serializers import UserDetailSerializer
from account.api.permissions import AnonPermissionOnly

from todos.api.serializers import TodosInlineUserSerializer

from todos.models import Todos

User = get_user_model()

class UserDetailApiView(generics.RetrieveAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # queryset = User.objects.filter(is_active=True)
    serializer_class = UserDetailSerializer
    lookup_field  = 'username'

    def get_serializer_context(self):
        return {'request': self.request}



class UserStatusAPIView(generics.ListAPIView):
    serializer_class = TodosInlineUserSerializer
    # pagination_class = CFEAPIPagination

    def get_queryset(self, *args, **kwargs):
        username = self.kwargs.get('username', None)
        if username is None:
            return Todos.objects.none()
        return Todos.objects.filter(user__username=username)
