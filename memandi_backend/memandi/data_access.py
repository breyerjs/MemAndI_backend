from django.contrib.auth.models import User
from django.db.models import Q

class Data_Access:
    def __init__(self):
        pass

    def create_user(self, username, first_name, last_name, email, password):
        new_user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password)
        return new_user

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
