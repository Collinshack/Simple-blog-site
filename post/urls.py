from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus', views.about_us, name='aboutus'),
    path('contactus', views.contact_us, name='contactus'),
    path('posts/<str:pk>', views.posts, name='posts'),
]