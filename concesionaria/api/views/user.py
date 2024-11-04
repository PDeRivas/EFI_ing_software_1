from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password

from django.contrib.auth.models import User

from api.serializers.user_serializer import UserSerializer
from rest_framework.permissions import IsAdminUser

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
            data = request.data

            #Hasheamos la contraseña, igual al metodo de la clase User
            password = data.get('password')
            hashPassword = make_password(password)

            user = User.objects.create(
                username=data.get('username'),
                password=hashPassword,
                first_name=data.get('first_name', None),
                last_name=data.get('last_name'),
                email=data.get('email')
            )

            serializer = self.serializer_class(user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
