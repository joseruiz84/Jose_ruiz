from django.shortcuts import render

def index(request):
    return render(request, "seguros/index.html")

def autos_1(request):
    return render(request, "seguros/autos.html")

def hogar_1(request):
    return render(request, "seguros/hogar.html")

def vida_1(request):
    return render(request, "seguros/vida.html")