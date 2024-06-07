from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'homepage'),
    path('register/', views.register, name = 'register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('deletetask/<str:todo3_name>/', views.DeleteTask, name='delete_todo3'),
    path('update/<str:todo3_name>/', views.Update, name='update'),



]