from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def catalog(request):
    return render(request, 'catalog.html')

def detailed_view(request):
    return render(request, 'detailed_view.html')

def checkout(request):
    return render(request, 'checkout.html')
