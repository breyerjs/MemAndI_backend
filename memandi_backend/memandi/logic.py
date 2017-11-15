from .data_access import Data_Access

class Logic:
    def __init__(self):
        pass

    def login_user(self, data):
        data_access = Data_Access()
        username = data['username']
        user = data_access.get_user_by_email_or_username(username=username)
        if user is None:
            return {"error": "Username does not exist."}
        if user.password != data['password']:
            return {"error": "Password is incorrect."}
        return data_access.get_auth_token(username)

    def create_user(self, user_serializer):
        data_access = Data_Access()
        # check if user exists by email / username
        existing_user = data_access.get_user_by_email_or_username(
            email=user_serializer.validated_data['email'],
            username=user_serializer.validated_data['username'])
        if existing_user is not None:
            return "That username or email is already taken"
        data_access.create_user(user_serializer)
        return None

    def create_memory(self, memory_serializer):
        Data_Access().create_memory(memory_serializer)
        return None

    def get_all_memories(self, user_id):
        return Data_Access().get_all_memories(user_id)
