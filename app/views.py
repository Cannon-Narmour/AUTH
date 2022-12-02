from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
# Create your views here.

def home(request):
    return render(request, "main.html")

def ambassadors(request):
    form = AmbassadorForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "ambassadors.html", {"form": form})

def detail(request):
    ambassadors = Ambassador.objects.all()
    return render(request, "detail.html", {"ambassadors" : ambassadors})

def update(request, id):
    ambassadors = Ambassador.objects.get(id=id)
    form = AmbassadorForm(request.POST, instance=ambassadors)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    return render(request, "update.html",{"ambassadors" : ambassadors})

def delete(request, id):
    form = Ambassador.objects.get(id=id)
    form.delete()
    return HttpResponseRedirect('/')

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


def sign_up(request):
    form = AmbassadorForm()
    if request.method == "POST":
        form = AmbassadorForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('signup')
    student = {"form": form}
    return render(request, "signup.html", student)
#Login in Page
def sign_in(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect("home")
    context = {}
    return render(request, "login.html", context)
#Log out Page
def log_out(request):
    logout(request)
    return redirect("logout")