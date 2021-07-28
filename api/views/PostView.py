from rest_framework import generics
from ..models import Post
from ..serializer import PostSerializer, PostListSerializer
from ..Paginations import PublicPagination
from rest_framework.permissions import AllowAny


class PostListView(generics.ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all().order_by('-createAt')
    pagination_class = PublicPagination
    permission_classes = [AllowAny]


class PostView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'
