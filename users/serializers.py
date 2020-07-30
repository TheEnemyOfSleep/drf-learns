from django.contrib.auth.models import Group, Permission
from .models import CustomUser
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('url', 'username', 'email', 'gender', 'profile_pic', 'groups', 'is_active', 'is_staff', 'date_joined')
        read_only_fields = ('is_active', 'is_staff', 'date_joined')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name', 'permissions')


class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission
        fields = ('url', 'name')


'''
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('url', 'username', 'email')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name', 'permissions')
        read_only_fields = ('permissions')


class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission
        fields = ('url', 'name')

'''