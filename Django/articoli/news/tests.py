from django.test import TestCase
from django.urls import resolve,reverse

from news.models import Giornalista
from news.views import homepage
# Create your tests here.

class HomePageViewTest(TestCase):
    def test1(self):
        view=resolve("/")
        print(view)
        self.assertEqual(view.func, homepage)

    def test2(self):
        url=reverse("homeview")
        print("url: ",url)
        response=self.client.get(url)
        print("response: ",response)
        self.assertEqual(response.status_code,200)
        
class GiornalistaTest(TestCase):
    def setUp(self):
        Giornalista.objects.create(nome='Pinco',cognome='Pallino')
    
    def test_giornalista(self):
        giornalista=Giornalista.objects.get(nome='Pinco')
        self.assertEqual(giornalista.__str__(),'Pinco Pallino')
