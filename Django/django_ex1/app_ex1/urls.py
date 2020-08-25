from django.urls import path
from app_ex1 import views as app_ex1_views

urlpatterns = [

    path('', app_ex1_views.homepage, name='home'),
path('/zafferano1', app_ex1_views.zafferano1, name='zafferano1'),
path('/zafferano2', app_ex1_views.zafferano2, name='zafferano2'),
path('/zafferano3', app_ex1_views.zafferano3, name='zafferano3'),


]
