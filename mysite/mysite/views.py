from django.http import HttpResponse

def aboutUs(request):
    return HttpResponse("Welcome to G Developer")


def gfolder(request):
    return HttpResponse("Wel-come to G folder...")


def gfile(request,gdevid):
    return HttpResponse(gdevid)