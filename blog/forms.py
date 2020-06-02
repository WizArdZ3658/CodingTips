from django import forms
from .models import Post, Comment
from pagedown.widgets import PagedownWidget


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=PagedownWidget)
    # publish = forms.DateTimeField(widget=forms.SelectDateWidget)

    class Meta:
        model = Post
        fields = ('title', 'content')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)