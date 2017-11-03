from .data_access import Data_Access

class Logic:
    def __init__(self):
        pass

    def create_user(self, username, first_name, last_name, email, password):
        data_access = Data_Access()
        # check if user exists by email / username
        existing_user = data_access.get_user_by_email_or_username(email=email, username=username)
        if len(existing_user) > 0:
            return "That username or email is already taken"
        data_access.create_user(username, first_name, last_name, email, password)
        return None
