from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    return render(request,"index.html")


def gfolder(request):
    return HttpResponse("Wel-come to G folder...")


def gfile(request,gdevid):
    return HttpResponse(gdevid)