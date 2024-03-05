from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "App/index.html")

def about(request):
    return render(request, "App/about.html")

def contact(request):
    return render(request, "App/contact.html")

def News(request):
    return render(request, "App/News.html")

def signup(request):
    return render(request, "App/signup.html")