from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.ReviewListCreateAPIView.as_view(), name='review-list-create'),
    path('', views.reviews_page, name='reviews-page'),

]

