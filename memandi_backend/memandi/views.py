from django.http import HttpResponse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .logic import Logic
from .serializers import UserSerializer, MemorySerializer

def index(request):
    return HttpResponse("Hello, world. You're at the memandi index.")

class UserList(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request, format='json'):
        user_serializer = UserSerializer(data=request.data)
        if not user_serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        errors = Logic().create_user(user_serializer)
        if errors is not None:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(user_serializer.validated_data, status=status.HTTP_201_CREATED)

class MemoryList(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request, user_id, format='json'):
        serializer = MemorySerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        errors = Logic().create_memory(serializer)
        if errors is not None:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, user_id, format=None):
        memories = Logic().get_all_memories(user_id)
        return Response(memories, status=status.HTTP_200_OK)
