from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer


class NoteModelViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)