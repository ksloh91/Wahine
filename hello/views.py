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

def assets_6_vehicles (request):
    # return HttpResponse('Hello from Python!')
    return render(request, "assets-6-vehicles.html")

def assets_7_others (request):
    # return HttpResponse('Hello from Python!')
    return render(request, "assets-7-others.html")


def index_v3 (request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index-v3.html")


def edits_assets_bank (request):
    # return HttpResponse('Hello from Python!')
    return render(request, "edits-assets-bank.html")

def edits_assets_epf (request):
    # return HttpResponse('Hello from Python!')
    return render(request, "edits-assets-epf.html")

def edits_assets_insurance (request):
    # return HttpResponse('Hello from Python!')
    return render(request, "edits-assets-insurance.html")

def edits_assets_investment (request):
    # return HttpResponse('Hello from Python!')
    return render(request, "edits-assets-investment.html")

def edits_assets_property (request):
    # return HttpResponse('Hello from Python!')
    return render(request, "edits-assets-property.html")

def edits_assets_vehicles (request):
    # return HttpResponse('Hello from Python!')
    return render(request, "edits-assets-vehicles.html")

def edits_assets_others (request):
    # return HttpResponse('Hello from Python!')
    return render(request, "edits-assets-others.html")

def liabilities_1_creditcard (request):
    # return HttpResponse('Hello from Python!')
    return render(request, "liabilities-1-creditcard.html")

def liabilities_2_personalloan (request):
    # return HttpResponse('Hello from Python!')
    return render(request, "liabilities-2-personalloan.html")

def liabilities_3_vehiclesloan (request):
    # return HttpResponse('Hello from Python!')
    return render(request, "liabilities-3-vehiclesloan.html")

def liabilities_4_property (request):
    # return HttpResponse('Hello from Python!')
    return render(request, "liabilities-4-property.html")

def liabilities_5_others (request):
    # return HttpResponse('Hello from Python!')
    return render(request, "liabilities-5-others.html")

def edits_liabilities_creditcard (request):
    # return HttpResponse('Hello from Python!')
    return render(request, "edits-liabilities-creditcard.html")

def edits_liabilities_personalloan (request):
    # return HttpResponse('Hello from Python!')
    return render(request, "edits-liabilities-personalloan.html")

def edits_liabilities_vehiclesloan (request):
    # return HttpResponse('Hello from Python!')
    return render(request, "edits-liabilities-vehiclesloan.html")

def edits_liabilities_property (request):
    # return HttpResponse('Hello from Python!')
    return render(request, "edits-liabilities-property.html")

def edits_liabilities_others (request):
    # return HttpResponse('Hello from Python!')
    return render(request, "edits-liabilities-others.html")

def overview_assets (request):
    # return HttpResponse('Hello from Python!')
    return render(request, "overview-assets.html")

def overview_liabilities (request):
    # return HttpResponse('Hello from Python!')
    return render(request, "overview-liabilities.html")



# Create your views here.


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
