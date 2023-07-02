from django.shortcuts import render, HttpResponse
from .forms import userform


# Create your views here.
def signup_view(r):
    form = userform
    return HttpResponse("<h1>welcome to youtube</h1>")


