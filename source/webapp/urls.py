
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from webapp.views import PostListView, PostCreateView, PostUpdateView, PostDetailView, delete_view, UserListView, \
    UserDetailView, UserUpdateView

app_name = 'webapp'

urlpatterns = [
    #url for Posts
    path('', PostListView.as_view(), name='index'),
    path('article/create', PostCreateView.as_view(), name='post_create'),
    path('article/<int:pk>/update', PostUpdateView.as_view(), name='post_update'),
    path('article/<int:pk>/view', PostDetailView.as_view(), name='post_detail'),
    path('article/<int:pk>/delete', delete_view, name='post_delete'),

    #url for Users
    path('users', UserListView.as_view(), name='user_list'),
    path('user/<int:pk>', UserDetailView.as_view(), name='user_detail'),
    path('user/<int:pk>/update', UserUpdateView.as_view(), name='user_update')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)