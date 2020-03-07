from rest_framework import serializers
from .models import Post, Comment

# inheriting from superclass/baseclass serializers, specifically inheriting from the Hyperlinked Model Serializer


class PostSerializer(serializers.ModelSerializer):
    # when we serialize stuff for a Post, we want to add comments to that and we're gonna set the comments using the comment_detail view, this is a 1 to many relationship so we can have more than one, and these will all be read-only
    # Return comments data as a string
    comments = serializers.StringRelatedField(
        many=True,
        read_only=True
    )
    #

    class Meta:
        model = Post
        fields = ('id', 'author', 'location', 'body', 'img_url', 'comments',)


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.StringRelatedField(
        read_only=True
    )

    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'body',)
