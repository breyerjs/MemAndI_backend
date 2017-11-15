from .models import User, Memory
from .serializers import MemorySerializer
from django.db.models import Q
from rest_framework.authtoken.models import Token

class Data_Access:
    def __init__(self):
        pass

    def create_user(self, user_serializer):
        user_serializer.save()

    def get_auth_token(self, username):
        return Token.objects.get(user__username=username)

    def get_user_by_email_or_username(self, **kwargs):
        username = kwargs.get("username")
        email = kwargs.get("email")
        # todo some error here?
        results = None
        if username is None and email is None:
            return None
        elif email is None and username is not None:
            results = User.objects.filter(username=username)
        elif email is not None and username is None:
            results = User.objects.filter(email=email)
        else:
            results = User.objects.filter(Q(email=email) | Q(username=username))
        if len(results) == 0:
            return None
        return results.first()

    def create_memory(self, user_serializer):
        user_serializer.save()

    def get_all_memories(self, user_id):
        memories = Memory.objects.filter(user=user_id)
        return MemorySerializer(memories, many=True).data
