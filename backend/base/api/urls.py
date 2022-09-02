from django.urls import path
from . import views
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    # path('', views.getRoutes),
    
    path('categories/', views.getCategories),
    path('notes/', views.getNotes),
    path('one/', views.getOneNote),
    path('register/', views.register),
    path('logout/',views.myLogout),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
