from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('post/', views.getPost),
    path('post/<str:pk>/', views.getSinglePost),
    path('createpost/', views.createPost),
    path('updatepost/<str:pk>/', views.updatePost),
    path('post/user/<str:pk>/', views.getUserAllPost),
    path('post/delete/<str:pk>/', views.deletePost),
    path('search/<str:pk>/', views.searchPost),
]