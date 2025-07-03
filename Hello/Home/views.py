from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('this is a home page')


def about(request):
    return HttpResponse('this is a about page')

def services(request):
    return HttpResponse('This is a services page')

def contact(request):
    return HttpResponse('This is a contact page')