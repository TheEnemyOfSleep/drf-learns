from rest_framework import serializers
from django.contrib.auth.models import Group, Permission
from .models import CustomUser
from notes.serializers import NoteSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    notes = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, 
        view_name='note-detail'
    )
    class Meta:
        model = CustomUser
        fields = [
            'url', 'id',
            'username', 'email', 'gender',
            'profile_pic', 'groups', 'is_active',
            'is_staff', 'date_joined', 'notes'
        ]
        read_only_fields = ['is_active', 'is_staff', 'date_joined', 'notes']
        extra_kwargs = {
            'url': {'lookup_field': 'username'},
        }

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name', 'permissions')


class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission
        fields = ('url', 'name')