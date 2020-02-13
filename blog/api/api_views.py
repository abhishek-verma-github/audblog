from .serializers import BlogSerializer
from rest_framework import viewsets
from blog.models import *
from users.models import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication


class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
