from productivity.views import advertisement_views as views 
from django.urls import path

urlpatterns = [
    path('list/', views.AdvertisementList, name='list'),
    path('list/<int:pk>/', views.AdvertisementDetailList, name='detail'),
    path('create/', views.AdvertisementCreate, name='create'),
    path('update/<int:pk>/', views.AdvertisementUpdate, name='update'),
    path('adminUpdate/<int:pk>/', views.AdvertisementAdminUpdate, name='adminUpdate'),
    path('delete/<int:pk>/', views.AdvertisementDelete, name='delete'),
    
]