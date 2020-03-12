from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(

        many=True,
        read_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'posts')

# Password hashing from https://hackernoon.com/110percent-complete-jwt-authentication-with-django-and-react-2020-iejq34ta

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class PostSerializer(serializers.ModelSerializer):
    # when we serialize data for a Post, we want to add its comments to that and we're gonna set the comments using the comment_detail view, this is a 1 to many relationship so we can have more than one, and these will all be read-only
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
