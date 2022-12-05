from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
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
    return HttpResponseRedirect("/")

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
