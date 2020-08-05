from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    author = serializers.HyperlinkedRelatedField(
        view_name='customuser-detail',
        lookup_field='username',
        many=False,
        read_only=True
    )
    class Meta:
        model = Note
        fields = ['url', 'id', 'title', 'body', 'author']
