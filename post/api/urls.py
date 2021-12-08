from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('post/', views.getPost),
    path('createpost/', views.createPost),
    path('updatepost/<str:pk>/', views.updatePost),
]