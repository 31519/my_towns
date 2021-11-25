from productivity.views import jobs_views as views 
from django.urls import path

urlpatterns = [
    path('list/', views.JobsList, name='list'),
    path('list/<int:pk>/', views.JobsDetailList, name='detail'),
    path('create/', views.JobsCreate, name='create'),
    path('update/<int:pk>/', views.JobsUpdate, name='update'),
    path('adminUpdate/<int:pk>/', views.JobsAdminUpdate, name='adminUpdate'),
    path('delete/<int:pk>/', views.JobsDelete, name='delete'),
    
]
