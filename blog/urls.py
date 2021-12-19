from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
]
