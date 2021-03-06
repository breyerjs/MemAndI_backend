from django.http import HttpResponse

from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .logic import Logic
from .serializers import UserSerializer, MemorySerializer

"""
Default permissions: permissions.IsOwner + IsAuthenticated
    Note: user_id from the route is authorized, no others are.
    Do not send 'user' in the body of requests
"""

def index(request):
    return HttpResponse("Thanks for your interest in MemAndI!")

class Login(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        data = request.data
        if None in [data.get('username'), data.get('password')]:
            return Response("Both email and password are required", status=status.HTTP_400_BAD_REQUEST)
        token = Logic().login_user(data)
        # ie. the attempt to fetch the token is exceptional
        if isinstance(token, dict):
            return Response(token, status=status.HTTP_400_BAD_REQUEST)

        return Response({'token': str(token)}, status=status.HTTP_200_OK)

class UserList(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request, format='json'):
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        errors = Logic().create_user(user_serializer)
        if errors is not None:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(user_serializer.validated_data, status=status.HTTP_201_CREATED)

class MemoryList(APIView):

    def post(self, request, user_id, format='json'):
        data = _get_request_data_and_add_user_from_route(request)
        serializer = MemorySerializer(data=data)
        serializer.is_valid(raise_exception=True)
        errors = Logic().create_memory(serializer)
        if errors is not None:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, user_id, format=None):
        memories = Logic().get_all_memories(user_id)
        return Response(memories, status=status.HTTP_200_OK)


"""
    Helpers
"""
def _get_request_data_and_add_user_from_route(request):
    data = request.data
    data['user'] = str(request.user.id)
    return data
