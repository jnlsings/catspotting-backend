from rest_framework import serializers
from .models import Post, Comment

# inheriting from superclass/baseclass serializers, specifically inheriting from the Hyperlinked Model Serializer


class PostSerializer(serializers.HyperlinkedModelSerializer):
    # when we serialize stuff for a Post, we want to add comments to that and we're gonna set the comments using the comment_detail view, this is a 1 to many relationship so we can have more than one, and these will all be read-only
    comments = serializers.HyperlinkedRelatedField(
        view_name='comment_detail',
        many=True,
        read_only=True
    )
    # how do we want this info to actually be returned

    class Meta:
        model = Post
        fields = ('id', 'author', 'location', 'body', 'img_url', 'comments',)


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.HyperlinkedRelatedField(
        view_name='post_detail',
        read_only=True
    )

    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'body',)
