from django.db import models
from django.urls import reverse

# Create your models here.

class Giornalista(models.Model):
    ''' il modello generico di un giornalista '''
    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome + " " + self.cognome

    class Meta:
        verbose_name = 'Giornalista'
        verbose_name_plural = 'Giornalisti'


class Articolo(models.Model):
    ''' il modello generico di un articolo di news '''
    titolo = models.CharField(max_length=100)
    contenuto = models.TextField()
    giornalista = models.ForeignKey(Giornalista, on_delete=models.CASCADE, related_name="articoli")

    def __str__(self):
        return self.titolo

    def get_absolute_url(self):
        return reverse("articolo_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Articolo'
        verbose_name_plural = 'Articoli'