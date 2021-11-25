from productivity.views import resell_views as views 
from django.urls import path

urlpatterns = [
    path('list/', views.ResellList, name='list'),
    path('list/<int:pk>/', views.ResellDetailList, name='detail'),
    path('create/', views.ResellCreate, name='create'),
    path('update/<int:pk>/', views.ResellUpdate, name='update'),
    path('adminUpdate/<int:pk>/', views.ResellAdminUpdate, name='adminUpdate'),
    path('delete/<int:pk>/', views.ResellDelete, name='delete'),
    
]
