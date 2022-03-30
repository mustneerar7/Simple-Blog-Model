from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# rest framework addons
from rest_framework import generics
from .serializers import PostSerialier

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'
class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = "__all__"
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']
class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

# views for RESTful api
class BlogAPIListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialier
class BlogAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialier

    
