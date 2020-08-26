from django.urls import path
from .views import homepage,ArticoloDetailView,ArticoloDetailViewCB,ArticoloListViewCB

urlpatterns = [

    path('', homepage, name='homeview'),
    #path('articolo/<int:pk>', ArticoloDetailView, name="articolo_detail"),
    path('articolo/<int:pk>', ArticoloDetailViewCB.as_view(), name="articolo_detail"),
    path('liasta_articoli/', ArticoloListViewCB.as_view(), name="lista_articoli"),
]