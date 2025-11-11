from django.shortcuts import render 
from django.http import HttpResponse
import datetime

# Create your views here.
def index(request):
    return HttpResponse("settime")

def current_datetime(request):
    now = datetime.datetime.now()
    display = f"<html><body><h2>Current date and time is {now}</h2></body></html>"
    return HttpResponse(display)
