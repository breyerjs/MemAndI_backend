from django.contrib.auth.models import User

class Data_Access:
    def __init__(self):
        pass

    def create_user(self, username, first_name, last_name, email, password):
        # todo
        User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

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
            return User.objects.filter(email=email | username=username)
