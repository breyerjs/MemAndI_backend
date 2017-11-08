from .data_access import Data_Access

class Logic:
    def __init__(self):
        pass

    def create_user(self, user_serializer):
        data_access = Data_Access()
        # check if user exists by email / username
        existing_user = data_access.get_user_by_email_or_username(
            email=user_serializer.validated_data['email'],
            username=user_serializer.validated_data['username'])
        if len(existing_user) > 0:
            return "That username or email is already taken"
        data_access.create_user(user_serializer)
        return None

    def create_memory(self, memory_serializer):
        Data_Access().create_memory(memory_serializer)
        return None
