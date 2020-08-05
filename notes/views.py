from rest_framework import viewsets
<<<<<<< HEAD
from rest_framework import permissions
from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer
from .permissions import IsOwnerAdminOrReadOnly
=======
from .models import Note
from .serializers import NoteSerializer

>>>>>>> 520291b2b15db9c48bf562f464a1c1b8761d8a3b

class NoteModelViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

<<<<<<< HEAD
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
=======
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
>>>>>>> 520291b2b15db9c48bf562f464a1c1b8761d8a3b
