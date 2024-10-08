
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('room/<str:pk>/', views.room, name='room'),
    path('profile/<str:pk>/',views.userProfile, name='profile'),
    
    path('create-room/', views.create_room, name='create-room'),
    path('update-room/<str:pk>', views.update_room, name='update-room'),
    path('delete-room/<str:pk>', views.delete_room, name='delete-room'),
    path('delete-message/<str:pk>', views.delete_message, name='delete-message'),


    # Login Form
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('register/', views.register_page, name='register'),
]
