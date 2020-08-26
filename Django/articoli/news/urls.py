from django.urls import path
from .views import homepage,articoloDetailView

urlpatterns = [

    path('', homepage, name='homeview'),
    path('articolo/<int:pk>', articoloDetailView, name="articolo_detail"),
]