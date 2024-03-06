from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data={
        'title': 'Home Page',
        'bdata':'G Developer site...',
        'clist': ['PHP','Java','Javascript']
    }
    return render(request,"index.html",data)


def gfolder(request):
    return HttpResponse("Wel-come to G folder...")


def gfile(request,gdevid):
    return HttpResponse(gdevid)