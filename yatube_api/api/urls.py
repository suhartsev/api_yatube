from django.urls import path, include

from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, GroupViewSet, PostViewSet

rout = DefaultRouter()

rout.register(
    'posts',
    PostViewSet,
    basename='posts'
)
rout.register(
    'groups',
    GroupViewSet,
    basename='groups'
)
rout.register(
    r'posts/(?P<id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(rout.urls))
]
