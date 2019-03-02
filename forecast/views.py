from django.shortcuts import render
from django.http import HttpResponse
from rhythm_master.test1 import *

# Create your views here.
def index(request):
    return HttpResponse("Hello World!")
    
def friend(request):
    return HttpResponse(Map.getData())
    
def guide(request):
    return HttpResponse(Guide.getData())
    
def starmall(request):
    return HttpResponse(StarMall.getData())