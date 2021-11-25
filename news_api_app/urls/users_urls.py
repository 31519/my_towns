from news_api_app.views import users_views as views 
from django.urls import path
from news_api_app.views.users_views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (

    TokenRefreshView,
)

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    path('users-list/', views.UserList, name="user-list"),
    path('user-profile', views.UserProfile, name="user-profile"),
    path('users-registration/', views.UserRegistration, name="user-list"),
]
