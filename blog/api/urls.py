from django.urls import path
from . import views
from rest_framework.authtoken import views as v
urlpatterns = [
    path('posts', views.PostListCreateAPIView.as_view(), name='post-list-create'),
    path('posts/<int:pk>', views.PostRetrieveUpdateDestroyAPIView.as_view(), name='post-detail'),
    path('comments', views.CommentListCreateView.as_view(), name='comment-list-create'),
    path('commment/<int:pk>', views.CommentRetrieveUpdateDestroyView.as_view(), name='comment-detail'),
    path('posts/<int:post_id>/comments/', views.PostCommentListView.as_view(), name='post-comments'),
    path('api-token-auth/', v.obtain_auth_token),

]

