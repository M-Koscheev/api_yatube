from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, GroupViewSet, CommentViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='v1-posts')
router.register('groups', GroupViewSet, basename='v1-groups')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='v1-comments')

urlpatterns = [
    path('v1/', include(router.urls))
]
