from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse

def Insert_school(request):
    QSSO=school.objects.all()
    d={'QSSO':QSSO}
    if request.method=='POST':
        sn=request.POST['scn']
        sp=request.POST['pn']
        sl=request.POST['sl']
        so=school.objects.get_or_create(schoolName=sn,principal=sp,location=sl)[0]
        so.save()
        QSSLO=school.objects.all()
        s={'QSSLO':QSSLO}
        return render (request,'display_school.html',d)  
    return render (request,'Insert_school.html',d)   

def insert_student(request):
    QSTO=student.objects.all()
    d={'QSTO':QSTO}
    if request.method=='POST':
        scn=request.POST['scn']
        slo=school.objects.get(schoolName=scn)
        sn=request.POST['sn']
        sid=request.POST['sid']
        so=student.objects.get_or_create(schoolName=slo,studentName=sn,studentID=sid)[0]
        so.save()
        QSSTO=student.objects.all()
        s={'QSSTO':QSSTO}
        return render (request,'display_student.html',s)  
    return render (request,'insert_student.html',d) 