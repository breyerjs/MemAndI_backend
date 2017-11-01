from .data_access import Data_Access

class Logic:
    def __init__(self):
        pass

    def create_user(self, username, first_name, last_name, email, password):
        # check if user exists by email / username
        existing_user = data_access.get_user_by_email_or_username(email=email, username=username)
        if len(existing_user) > 0:
            return create_400_response("User already exists")
        result = Data_Access().create_user(username, first_name, last_name, email, password)
        return result

    def create_400_response(error):
        context = {
            'status': '400', 'error': error
        }
        response = HttpResponse(json.dumps(context), content_type='application/json')
        response.status_code = 400
        return response
