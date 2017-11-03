import json
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
            return create_400_response("Missing required field: " + field)
    # No need to check credentials since they haven't made any yet.

    error = Logic().create_user(
        body["username"],
        body["first_name"],
        body["last_name"],
        body["email"],
        body["password"])
    if error is not None:
        return create_400_response(error)
    return HttpResponse(status=204)
"""
    Helpers
"""

def get_request_body(request):
    body_unicode = request.body.decode('utf-8')
    return json.loads(body_unicode)

def create_400_response(error):
    context = {
        'status': '400', 'error': error
    }
    response = HttpResponse(json.dumps(context), content_type='application/json')
    response.status_code = 400
    return response
