from django.shortcuts import render, redirect
from . import models

def index(request):
    return render(request, "interests/index.html")

def process(request):
    user = models.User.objects.create(name=request.POST['name'], interest=request.POST['interest'])
    print "user created"
    return redirect("/show")


def show(request):
    users = models.User.objects.all()
    context = {'users': users}
    print "all user:"
    return render(request, "interests/list.html", context)

def interests(request, id):
    print "8888888888888888888888888", id
    user = models.User.objects.get(id=id)
    print user
    interest = models.Interest.objects.filter(user__id=id)
    context = {'user': user, 'interest':interest}
    print "all interests:"
    return render(request, "interests/interests.html", context)


# def process(request):
#     return render(request, "interests/index.html")
