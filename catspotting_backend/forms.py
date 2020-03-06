from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'location', 'body', 'image_url',)


class CommentForm(forms.ModelForm):

    class meta:
        model = Comment
        fields = ('post', 'author', 'body',)
