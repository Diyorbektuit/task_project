from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_login, name='admin_login'),
    path('logout/', views.admin_logout, name='admin_logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('<str:model_name>/', views.model_list, name='model_list'),
    path('<str:model_name>/create/', views.model_create, name='model_create'),
    path('<str:model_name>/update/<int:pk>/', views.model_update, name='model_update'),
    path('<str:model_name>/delete/<int:pk>/', views.model_delete, name='model_delete'),
]
