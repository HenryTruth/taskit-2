from rest_framework import serializers

from account.api.serializers import UserPublicSerializer
from rest_framework.reverse import reverse as api_reverse
from todos.models import Todos


class TodosInlineUserSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Todos
        fields = [
            'uri',
            'id',
            'title', 
            'completed'
        ]

    def get_uri(self, obj):
        return "api/todos/{id}/".format(id=obj.id)



class TodosSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    user = UserPublicSerializer(read_only=True)

    class Meta:
        model = Todos
        fields = [
            'uri',
            'id',
            'user',
            'title', 
            'completed'
        ]

        read_only_fields = ['user']

    def get_uri(self, obj):
        return "api/todos/{id}/".format(id=obj.id)
    
    def validate_title(self, value):
        if len(value)  > 100:
            raise serializers.ValidationError("This is way to short")
        return value