from django.urls import path
from .views import homepage, zafferano1, zafferano2, zafferano3

urlpatterns = [

    path('', homepage, name='home'),
    path('zafferano1/', zafferano1, name='zafferano1'),
    path('zafferano2/', zafferano2, name='zafferano2'),
    path('zafferano3/', zafferano3, name='zafferano3'),

]
