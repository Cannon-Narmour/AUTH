from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    return render(request, "main.html")

def ambassadors(request):
    return render(request, "ambassadors.html")


def dashboard (request):
    orders = Order.objects.all()
    ambassadors = Ambassador.objects.all()

    #TOTAL
    t_ambassadors = ambassadors.count()
    t_orders = orders.count()

    #Order Information
    completed = orders.filter(status="Delivered").count()
    pending = orders.filter(status="Pending").count()

    #Dict.
    information = {"orders":orders ,"ambassadors":ambassadors, "t_orders":t_orders, "completed":completed, "pending":pending}

    return render(request, "dashboard.html",information)

def jobs (request):
    jobs = Job.objects.all()
    return render(request, "jobs.html",{"jobs":jobs})
