from django.http import HttpResponse
from django.template import loader
from .models import Member

def produits(request):
  myproduits = produits.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'myme': mymembers,
  }
  return HttpResponse(template.render(context, request))