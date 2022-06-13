from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from rest_framework_simplejwt.views import TokenViewBase
from user.serializers import CustomTokenObtainSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import status
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework.decorators import api_view, permission_classes
from .models import User
from .serializers import *



class CustomTokenView(TokenViewBase):
    serializer_class = CustomTokenObtainSerializer
    permission_classes = ([AllowAny])
    def post(self, request, *args, **kwargs):
        try:
            user_obj = User.objects.filter(Q(phone_number=request.data["phone_number"] )).first()
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                data = serializer.validated_data
                user = UserSerializer(user_obj)
                data['user'] = user.data
                return Response(data, status=status.HTTP_200_OK)

        except TokenError as e:
            raise InvalidToken(e.args[0])

        except User.DoesNotExist:
            return Response("Can't find user", status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def createUser(request):
    serialize = CustomUserSerializer(data=request.data)
    if serialize.is_valid():
        serialize.save()
        return Response({'data': serialize.data}, status=status.HTTP_201_CREATED)

    return Response({'data': serialize.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def users(request):
    items = User.objects.all()
    serialize = UserSerializer(items, many=True)
    return Response({'data': serialize.data}, status=status.HTTP_200_OK)
