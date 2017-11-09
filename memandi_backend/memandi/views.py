from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .logic import Logic
from .serializers import UserSerializer, MemorySerializer


def index(request):
    return HttpResponse("Hello, world. You're at the memandi index.")

@api_view(['POST'])
@authentication_classes(())
@permission_classes(())
def create_user(request):
    if request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            errors = Logic().create_user(user_serializer)
        if errors is None:
            return Response(user_serializer.validated_data, status=status.HTTP_201_CREATED)
        else:
            return Response(errors, status=400)

@api_view(['POST'])
def create_memory(request, user_id):
    if request.method == 'POST':
        data = request.data
        serializer = MemorySerializer(data=data)
        if serializer.is_valid():
            errors = Logic().create_memory(serializer)
            if errors is None:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(errors, status=400)
        return Response(status=400)
