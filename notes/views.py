from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer
from .permissions import IsOwnerAdminOrReadOnly

class NoteModelViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_permissions(self):
        if self.action in ['update', ]:
            self.permission_classes = [IsOwnerAdminOrReadOnly]
        return super(self.__class__, self).get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    # def get_queryset(self):
    #     queryset = self.queryset.filter(author=self.request.user)
    #     return queryset


class NotesList(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer