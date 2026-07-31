from django.shortcuts import render, redirect
from .models import Produits

def produits(request):
    myproduits = Produits.objects.all()
    return render(request, "index.html", context={"mon_produit": myproduits,})