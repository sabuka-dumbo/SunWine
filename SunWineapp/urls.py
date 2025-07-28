from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('services/', views.services, name="services"),
    path('gallery/', views.gallery, name="gallery"),
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('booking/', views.booking, name="booking"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('room/<int:roomid>/', views.room, name="room"),
    path('bought/', views.bought, name="bought"),

    path('dashboard1/', views.dashboard1, name="dashboard1"),
]