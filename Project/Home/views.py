from django.shortcuts import render, HttpResponse
from .models import product

# Create your views here.
def index(request):
    products = product.objects.all()
    return render(request, 'index.html', {'products':products})
    # return HttpResponse('this is a home page')


def about(request):
    return HttpResponse('this is a about page')

def services(request):
    return HttpResponse('This is a services page')

def contact(request):
    return HttpResponse('This is a contact page')