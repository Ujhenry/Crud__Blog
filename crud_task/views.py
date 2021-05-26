from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post


# Create your views here.
class CrudListView(ListView):
    model = Post
    template_name = 'home.html'

class CrudDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class CrudCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class CrudUpdatedView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class CrudDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
