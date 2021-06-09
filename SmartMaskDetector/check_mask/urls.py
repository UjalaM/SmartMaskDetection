from django.contrib import admin
from django.urls import path,include
from check_mask import views

app_name='check_mask'

urlpatterns = [
    path('webcam', views.webcam,name="webcam"),
    path('mail', views.send_mail,name="send_mail"),
    path('video_feed', views.video_feed, name='video_feed'),
]