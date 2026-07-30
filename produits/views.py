from django.shortcuts import render, redirect
from .models import Produits
from .forms import ProduitsForm

def produits(request):
    if request.method == "POST":
        form = ProduitsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = ProduitsForm()

    myproduits = Produits.objects.all()
    return render(request, "index.html", context={"mon_produit": myproduits, "form": form})