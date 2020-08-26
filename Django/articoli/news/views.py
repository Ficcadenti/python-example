from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from articoli.settings import BASE_DIR
from .models import Giornalista, Articolo

# Create your views here.

'''
def homepage(request):
    a = []
    g = []

    for art in Articolo.objects.all():
        a.append(art.titolo)

    for gio in Giornalista.objects.all():
        g.append(gio.nome)

    respone = "<h1>" + str(a) + "<br>" + str(g) + "</h1>"
    print(respone)
    return HttpResponse(respone)
'''


def homepage(request):
    articoli = Articolo.objects.all()
    giornalisti = Giornalista.objects.all()

    context = {"giornalisti": giornalisti, "articoli": articoli}
    print(context)

    for g in giornalisti:
        print(g)
        for a in g.articoli.all():
            print(a.titolo)


    return render(request, "content.html", context)


def ArticoloDetailView(request,pk):
    # Articolo.objects.get(pk=pk)
    articolo = get_object_or_404(Articolo,pk=pk)
    context = {"articolo": articolo}
    return render(request, "../templates/articolo_detail.html", context)

## GCBV Class Based View

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

class ArticoloDetailViewCB(DetailView):
    model = Articolo
    template_name = 'articolo_detail.html'

class ArticoloListViewCB(ListView):
    model = Articolo
    template_name = 'lista_articoli.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["articoli"]=Articolo.objects.all()
        return context