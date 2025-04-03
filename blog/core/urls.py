from django.urls import path
from .views import (PostListView, PostCreateView, PostDetailView,
                    UserLoginView, UserLogoutView, UserRegisterView)
urlpatterns = [
    path('index/', PostListView.as_view(), name='index'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register', UserRegisterView.as_view(), name='register'),
]