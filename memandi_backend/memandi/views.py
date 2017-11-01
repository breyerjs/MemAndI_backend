from django.shortcuts import render
from django.http import HttpResponse
from .logic import Logic

def index(request):
    return HttpResponse("Hello, world. You're at the memandi index.")

def create_user(request):
    body = get_request_body(request)
    expected_fields = ["username", "first_name", "last_name", "email", "password"]
    for field in expected_fields:
        if field not in body:
            return create_missing_argument_400_response(field)
    # No need to check credentials since they haven't made any yet.
    result = Logic().create_user(username, first_name, last_name, email, password)


"""
    Helpers
"""

def get_request_body(request):
    body_unicode = request.body.decode('utf-8')
    return json.loads(body_unicode)

def create_missing_argument_400_response(argument_name):
    context = {
        'status': '400', 'missing_argument': argument_name
    }
    response = HttpResponse(json.dumps(context), content_type='application/json')
    response.status_code = 400
    return response
