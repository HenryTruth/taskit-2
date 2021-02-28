import datetime
from django.contrib.auth import get_user_model

from django.utils import timezone
from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from todos.api.serializers import TodosInlineUserSerializer


User = get_user_model()

class UserDetailSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    todos = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'uri',
            'todos'
        ]
        
 
    def get_uri(self, obj):
        return api_reverse("api_user:detail", kwargs={"username":obj.username}, request=request)

    def get_todos(self, obj):
        request = self.context.get('request') 
        limit = 10
        if request:
            limit = request.GET.get('limit')
            try:
                limit = int(limit_query)
            except:
                pass
        qs = obj.todos_set.all()
        data = {
            'uri':self.get_uri(obj) + "todos/",
            'last': TodosInlineUserSerializer(qs.first()).data,
            'recent':TodosInlineUserSerializer(qs[:limit], many=True).data
        }
        return data
 
    # def get_recent_todos(self, obj):
    #     qs = obj.todos_set.all()
    #     return 
