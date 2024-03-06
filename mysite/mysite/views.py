from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data={
        'title': 'Home Page',
        'bdata':'G Developer site...',
        'clist': ['Html','Css','Javascript','C','Python','Django','MySQL','Git','Github','Ms-excel'],
        'student_details':[
            {'name':'Robin','age':21,'phone':9876543210},
            {'name':'Toni','age':37,'phone':1234567890},
            {'name':'Jasmin','age':18,'phone':9988667733},
            {'name':'Kaniya','age':24,'phone':8877755999},
            {'name':'Robin 2','age':20,'phone':9988544444},
        ]
    }
    return render(request,"index.html",data)


def gfolder(request):
    return HttpResponse("Wel-come to G folder...")


def gfile(request,gdevid):
    return HttpResponse(gdevid)