from productivity.views import shops_views as views 
from django.urls import path

urlpatterns = [
    path('list/', views.ShopsList, name='list'),
    path('list/<int:pk>/', views.ShopsDetailList, name='detail'),
    path('create/', views.ShopsCreate, name='create'),
    path('update/<int:pk>/', views.ShopsUpdate, name='update'),
    path('adminUpdate/<int:pk>/', views.ShopsAdminUpdate, name='adminUpdate'),
    path('delete/<int:pk>/', views.ShopsDelete, name='delete'),
    
]
