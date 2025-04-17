from rest_framework import serializers
from core.models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'author_username', 'content', 'created_at']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        validated_data.pop('author', None)  # optional, to avoid duplicate if present
        return Comment.objects.create(author=user, **validated_data)


class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'image_path', 'content', 'author', 'author_username', 'created_at', 'updated_at', 'comments']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        validated_data.pop('author', None)  # optional, to avoid duplicate if present
        return Post.objects.create(author=user, **validated_data)
