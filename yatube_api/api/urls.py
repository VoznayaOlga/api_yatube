from rest_framework.authtoken import views
from rest_framework import routers
from django.urls import path, include

from .views import PostViewSet, GroupViewSet, CommentViewSet

v1_router = routers.SimpleRouter()
v1_router.register('posts', PostViewSet, basename='posts')
v1_router.register('groups', GroupViewSet, basename='groups')
v1_router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                   basename='comments')

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(v1_router.urls)),

]
