from django.shortcuts import render
from .models import Photorecorder
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/account/login/')
def user(request):
    Photorec = Photorecorder.objects.all()
    return render(request, 'photographer.html',{'Photorec' : Photorec})