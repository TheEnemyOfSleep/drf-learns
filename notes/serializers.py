from rest_framework import serializers
from .models import Note

<<<<<<< HEAD
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
=======
class NoteSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Note
    fields = ['url', 'id', 'title', 'body', 'author']
>>>>>>> 520291b2b15db9c48bf562f464a1c1b8761d8a3b
