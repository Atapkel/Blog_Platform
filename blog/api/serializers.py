from rest_framework import serializers
from core.models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'author_username', 'content', 'created_at']

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("Comment content cannot be empty.")
        if len(value) > 1000:
            raise serializers.ValidationError("Comment is too long (max 1000 characters).")
        return value

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        validated_data.pop('author', None)
        return Comment.objects.create(author=user, **validated_data)


class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.SerializerMethodField(method_name='get_comment_count')
    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'image_path', 'content', 'author',
                  'author_username', 'created_at', 'updated_at', 'comments',
                  'comments_count']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        validated_data.pop('author', None)
        return Post.objects.create(author=user, **validated_data)

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty.")
        if len(value) > 255:
            raise serializers.ValidationError("Title is too long (max 255 characters).")
        return value

    def get_comment_count(self, obj):
        return obj.comments.count()


class PostInfoSerializer(serializers.Serializer):
    tech = serializers.IntegerField()
    life = serializers.IntegerField()
    edu = serializers.IntegerField()
    other = serializers.IntegerField()