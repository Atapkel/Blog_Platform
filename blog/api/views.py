from core.models import Comment, Post
from rest_framework.decorators import api_view
from .serializers import CommentSerializer, PostSerializer, PostInfoSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response

class PostListCreateAPIView(generics.ListCreateAPIView):
    # queryset = Post.objects.all()
    queryset = Post.objects.select_related("author").prefetch_related("comments")
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Post.objects.all()
    queryset = Post.objects.select_related("author").prefetch_related("comments")
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class CommentListCreateView(generics.ListCreateAPIView):
    # queryset = Comment.objects.all()
    queryset = Comment.objects.select_related("author", "post")
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Comment.objects.all()
    queryset = Comment.objects.select_related("author", "post")
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PostCommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post__id=post_id)

@api_view(['GET'])
def info(request):
    posts = Post.objects.all()
    tech_count = posts.filter(category=Post.CategoryChoices.TECH).count()
    life_count = posts.filter(category=Post.CategoryChoices.LIFE).count()
    edu_count = posts.filter(category=Post.CategoryChoices.EDU).count()
    other_count = posts.filter(category=Post.CategoryChoices.OTHER).count()
    serializer = PostInfoSerializer({
        'tech': tech_count,
        'life': life_count,
        'edu': edu_count,
        'other': other_count
    })
    return Response(serializer.data)