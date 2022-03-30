from django.urls import path
from django.urls.conf import include
from .views import BlogDetailView, BlogListView, BlogCreateView, BlogUpdateView, BlogDeleteView

# rest framework specific views
from .views import BlogAPIDetailView, BlogAPIListView

urlpatterns = [
    path('', BlogListView.as_view(), name="home"),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='details'),
    path('/new',BlogCreateView.as_view(), name="post_new"),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/',BlogDeleteView.as_view(), name='post_delete'),

    #rest framework specific endpoints
    path('api/v1/', BlogAPIListView.as_view(), name = "v1 endpoint"),
    path('api/v1/<int:pk>/', BlogAPIDetailView.as_view(), name = "endpoint details"),
]