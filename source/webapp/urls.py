
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from webapp.views import PostListView, PostCreateView, PostUpdateView, PostDetailView

app_name = 'webapp'

urlpatterns = [
    #url for Posts
    path('', PostListView.as_view(), name='index'),
    path('article/create', PostCreateView.as_view(), name='post_create'),
    path('article/<int:pk>/update', PostUpdateView.as_view(), name='post_update'),
    path('article/<int:pk>/view', PostDetailView.as_view(), name='post_detail')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)