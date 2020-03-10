from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(
        # view_name='post_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'posts')


class PostSerializer(serializers.ModelSerializer):
    # when we serialize stuff for a Post, we want to add comments to that and we're gonna set the comments using the comment_detail view, this is a 1 to many relationship so we can have more than one, and these will all be read-only
    # Return comments data as a string
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.StringRelatedField(
        many=True,
        read_only=True
    )

    class Meta:
        model = Post
        fields = ('id', 'owner', 'location', 'body', 'img_url', 'comments',)


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    post = serializers.StringRelatedField(
        read_only=True
    )

    class Meta:
        model = Comment
        fields = ('id', 'owner', 'post', 'body',)


class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
