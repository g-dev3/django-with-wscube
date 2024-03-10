from django.http import HttpResponse
from django.shortcuts import render

data={
        'title': 'Home Page',
        'title1': 'About us',
        'bdata':'G Developer site...',
        'clist': ['Html','Css','Javascript','C','Python','Django','MySQL','Git','Github','Ms-excel'],
        'student_details':[
            {'name':'Robin','age':21,'phone':9876543210},
            {'name':'Toni','age':37,'phone':1234567890},
            {'name':'Jasmin','age':18,'phone':9988667733},
            {'name':'Kaniya','age':24,'phone':8877755999},
            {'name':'Robin 2','age':20,'phone':9988544444},
        ],
        'numbers':[]
        # 10,20,30,40,50
    }
def homePage(request):
    
    return render(request,"index.html",data)


def aboutUs(request):
    return render(request,'about-us.html',data)


def profileCard(request):
    return render(request,'index1.html')



def gfile(request,gdevid):
    return HttpResponse(gdevid)


def userForm(request):
    formdata=0
    fdata={}
    try:
        if request.method == "POST":
        # n1 = int(request.GET['num1'])
        # n2 = int(request.GET['num2'])
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            formdata = n1 + n2
            fdata={
                'n1':n1,
                'n2':n2,
                'output':formdata
            }
            
    except:
        pass
    return render(request,'form.html',fdata)
