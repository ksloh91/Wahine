from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index_v2(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index-v2.html")


def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def joinnow(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "joinnow.html")

def createaccount (request):
    # return HttpResponse('Hello from Python!')
    return render(request, "createaccount.html")



# Create your views here.


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
