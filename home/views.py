from django.shortcuts import render
from .forms import userform


# Create your views here.
def signup_view(r):
    form = userform
    return render(r, 'index.html', {'form':form})


