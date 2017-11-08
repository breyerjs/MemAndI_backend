from .models import User
from django.db.models import Q

class Data_Access:
    def __init__(self):
        pass

    def create_user(self, user_serializer):
        user_serializer.save()

    def get_user_by_email_or_username(self, **kwargs):
        username = kwargs["username"]
        email = kwargs["email"]
        # todo some error here?
        if username is None and email is None:
            return None
        elif email is None and username is not None:
            return User.objects.filter(username=username)
        elif email is not None and username is None:
            return User.objects.filter(email=email)
        else:
            return User.objects.filter(Q(email=email) | Q(username=username))

    def create_memory(self, user_serializer):
        user_serializer.save()
