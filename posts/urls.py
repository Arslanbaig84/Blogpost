from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.posts, name='posts'),
    path('new_post/', views.new_post, name='new_post'),
    path('<slug:slug>/', views.post, name='post'),
]