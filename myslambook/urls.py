from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:slam_id>', views.details, name='details'),
    path('addnewslam/<str:user_id>', views.addnewslam, name='addnewslam'),
    path('delete', views.delete, name='delete'),
    path('register', views.register, name='register'),
    path('userlogin', views.userlogin, name='userlogin'),
    path('userlogout', views.userlogout, name='userlogout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('share', views.share, name='share'),
    path('birthdays', views.birthdays, name='birthdays'),
    path('demo', views.demo, name='demo'),
]

