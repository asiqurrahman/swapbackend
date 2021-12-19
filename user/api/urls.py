from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from .views import CreateUserView
from .views import MyTokenObtainPairView


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('user/', views.getUser),
    path('register/', CreateUserView.as_view()),
    path('token/', MyTokenObtainPairView .as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/<str:pk>/', views.getSingleUser),
    path('user/update/<str:pk>/', views.updateUser),
]