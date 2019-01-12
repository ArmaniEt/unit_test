from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from webapp.forms import PostForm
from django.urls import reverse_lazy


"""
Creating CRUD for Posts
"""


class PostListView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    model = Post

    def get_queryset(self):
        return self.model.objects.order_by('-date')


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'post_create.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('webapp:index')


class FoodUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_update.html'
    form_class = PostForm
    success_url = reverse_lazy('index')