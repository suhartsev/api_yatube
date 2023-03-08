from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, GroupViewSet, PostViewSet

route_v1 = DefaultRouter()

route_v1.register(
    'posts',
    PostViewSet,
    basename='posts'
)
route_v1.register(
    'groups',
    GroupViewSet,
    basename='groups'
)
route_v1.register(
    r'posts/(?P<id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(route_v1.urls))
]
