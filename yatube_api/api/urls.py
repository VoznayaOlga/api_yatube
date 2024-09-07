from rest_framework.authtoken import views
from rest_framework_nested import routers

from django.urls import path, include

from .views import PostViewSet, GroupViewSet, CommentViewSet

router = routers.SimpleRouter()
router.register('posts', PostViewSet)
com_router = routers.NestedSimpleRouter(router, 'posts', lookup='posts')
com_router.register('comments', CommentViewSet)
router.register('groups', GroupViewSet)


urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include(com_router.urls)),
]
