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

def subsuccessful (request):
    # return HttpResponse('Hello from Python!')
    return render(request, "subsuccessful.html")

def accountinfo (request):
    # return HttpResponse('Hello from Python!')
    return render(request, "accountinfo.html")

def assets (request):
    # return HttpResponse('Hello from Python!')
    return render(request, "assets.html")

def assets_2_epf (request):
    # return HttpResponse('Hello from Python!')
    return render(request, "assets-2-epf.html")

def assets_3_insurance (request):
    # return HttpResponse('Hello from Python!')
    return render(request, "assets-3-insurance.html")

def assets_4_investment (request):
    # return HttpResponse('Hello from Python!')
    return render(request, "assets-4-investment.html")

def assets_5_property (request):
    # return HttpResponse('Hello from Python!')
    return render(request, "assets-5-property.html")

# Create your views here.


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
