from rest_framework.authtoken import views
from rest_framework import routers

from django.urls import path, include

from .views import PostViewSet, GroupViewSet, CommentViewSet

router = routers.SimpleRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)

urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('api/v1/', include(router.urls)),

]
