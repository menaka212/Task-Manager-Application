from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('move/<int:pk>/<str:stage>/', views.move_task, name='move_task'),
]