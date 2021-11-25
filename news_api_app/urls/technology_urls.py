from news_api_app.views import technology_views as views 
from django.urls import path

urlpatterns = [
    path('list/', views.TechnologyList, name="list"),
    path('list/<int:pk>', views.TechnologyDetailList, name="detail"),
    path('delete/<int:pk>', views.TechnologyDelete, name="delete"),
    path('create/', views.TechnologyCreate, name='create'),
    path('update/<int:pk>/', views.TechnologyUpdate, name='update')
]
