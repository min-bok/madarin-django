from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post


# Create your views here.
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/post_create.html'
    fields = ['image', 'caption']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RegistraterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('market:post_list')