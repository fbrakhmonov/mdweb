from django import forms
from convertor.models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'summary', 'page_md']
