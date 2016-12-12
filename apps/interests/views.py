from django.shortcuts import render, redirect

def index(request):
    return render(request, "interests/index.html")

def process(request):
    return render(request, "interests/list.html")

# def process(request):
#     return render(request, "interests/index.html")
