from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    return render(request, "index.html")

def customers(request):
    return render(request, "customers.html")


def dashboard (request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    #TOTAL
    t_customers = customers.count()
    t_orders = orders.count()

    #Order Information
    completed = orders.filter(status="Delivered").count()
    pending = orders.filter(status="Pending").count()

    #Dict.
    information = {"orders":orders ,"customers":customers, "t_orders":t_orders, "completed":completed, "pending":pending}

    return render(request, "dashboard.html",information)

def jobs (request):
    jobs = Job.objects.all()
    return render(request, "jobs.html",{"jobs":jobs})
