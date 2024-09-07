from rest_framework import serializers

from posts.models import Post, Group, Comment, User


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'post', 'text', 'created', 'author',)
        read_only_fields = ('author', 'created', 'post')

    def get_author(self, obj):
        return User.objects.get(id=obj.author_id).username


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'image', 'group', 'author',
                  'comments')
        read_only_fields = ('author', 'id',)

    def get_author(self, obj):
        return User.objects.get(id=obj.author_id).username


class GroupSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description', 'posts',)
