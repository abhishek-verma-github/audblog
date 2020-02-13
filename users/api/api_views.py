from .serializers import UserSerializer
from rest_framework import viewsets
from blog.models import *
from users.models import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
