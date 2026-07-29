from django.shortcuts import render

def index(request):
    date="10-09-2026"
    return render(request,'index.html', context={"name": date})

