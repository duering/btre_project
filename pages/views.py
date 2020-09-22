from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

# def example_with_http_response(request):
#     return HttpResponse('<h1>Hello World</h1>')