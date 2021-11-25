from productivity.views import tourisms_views as views 
from django.urls import path

urlpatterns = [
    path('list/', views.TourismsList, name='list'),
    path('list/<int:pk>/', views.TourismsDetailList, name='detail'),
    path('create/', views.TourismsCreate, name='create'),
    path('update/<int:pk>/', views.TourismsUpdate, name='update'),
    path('adminUpdate/<int:pk>/', views.TourismsAdminUpdate, name='adminUpdate'),
    path('delete/<int:pk>/', views.TourismsDelete, name='delete'),
    
]