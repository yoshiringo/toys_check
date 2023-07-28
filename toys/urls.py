from django.urls import path
from . import views

app_name = 'toys'

urlpatterns = [
    path('', views.Index.as_view(), name = 'index'),
    path('register', views.Register.as_view(), name = 'register'),
    path('delete/<int:pk>/', views.ToysDeleteView.as_view(), name = 'delete'), 
    path('update/<int:pk>/', views.ToysUpdateView.as_view(), name = 'update'), 
]