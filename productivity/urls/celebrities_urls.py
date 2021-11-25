from productivity.views import celebrities_views as views 
from django.urls import path

urlpatterns = [
    path('list/', views.CelebritiesList, name='list'),
    path('list/<int:pk>/', views.CelebritiesDetailList, name='detail'),
    path('create/', views.CelebritiesCreate, name='create'),
    path('update/<int:pk>/', views.CelebritiesUpdate, name='update'),
    path('adminUpdate/<int:pk>/', views.CelebritiesAdminUpdate, name='adminUpdate'),
    path('delete/<int:pk>/', views.CelebritiesDelete, name='delete'),
    
]
