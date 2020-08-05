from django.contrib.auth.models import Group, Permission
from .models import CustomUser
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, PermissionSerializer
from rest_framework.mixins import RetrieveModelMixin


class UserViewSet(viewsets.ModelViewSet, RetrieveModelMixin):
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    lookup_field = "username"


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PermissionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer