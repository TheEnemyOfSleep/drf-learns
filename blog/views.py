from rest_framework import viewsets
from .models import Post, Tag
from .serializers import PostSerializer, TagSerializer

class PostModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-date_pub')
    serializer_class = PostSerializer


class TagModelViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer