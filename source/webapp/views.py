from django.views.generic import ListView, DetailView, CreateView, UpdateView
from webapp.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from webapp.forms import PostForm
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.http import Http404


"""
Creating CRUD for Posts
"""


class PostListView(ListView):
    template_name = 'index.html'
    model = Post

    def get_queryset(self):
        return self.model.objects.order_by('-date')


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'post_create.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('webapp:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_update.html'
    form_class = PostForm

    def dispatch(self, request,  *args, **kwargs):
        user = get_object_or_404(Post, pk=kwargs.get('pk'))
        if user.author == request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_view.html'


def delete_view(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if post.author == request.user:
        post.delete()
        return redirect('webapp:index')
    else:
        raise Http404