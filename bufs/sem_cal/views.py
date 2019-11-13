from django.shortcuts import render
from django.http import HttpResponse
from sem_cal import models
# Create your views here.
def index(request):
    all_sems=models.Seminar.objects.order_by('-date')
    past_sems=[a for a in all_sems if a.is_past()]
    future_sems=[a for a in all_sems if not a.is_past()][::-1]
    context={'upcoming_seminars':future_sems,'past_seminars':past_sems}
    return render(request,'sem_cal/index.html',context)

def detail(request,id):
    sem=models.Seminar.objects.get(id=id)
    context={'sem':sem}
    return render(request,'sem_cal/detail.html',context)

def about(request):
    return render(request,'sem_cal/about.html',{})
