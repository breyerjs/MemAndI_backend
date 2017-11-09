from rest_framework import serializers
from .models import User, Memory

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'password', 'email')


class MemorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField(max_length=1000)
    pub_date = serializers.DateTimeField()
    starred = serializers.BooleanField()
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Memory
        fields = ('id', 'text', 'pub_date', 'starred', 'user')
        # for auth
        owner = serializers.ReadOnlyField(source='user.username')
