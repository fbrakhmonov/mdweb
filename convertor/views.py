from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from convertor.models import Post
from django.urls import reverse_lazy
from convertor.forms import PostCreateForm


class PostCreateViewPage(CreateView):
    template_name = 'pages/post_create_page.html'
    form_class = PostCreateForm
    success_url = reverse_lazy('convertor:post-list')


class PostListViewPage(ListView):
    template_name = 'pages/post_list_page.html'
    model = Post


class PostDetailViewPage(DetailView):
    template_name = 'pages/post_detail_page.html'
    model = Post
