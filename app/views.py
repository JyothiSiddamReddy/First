from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def jyothi(request):
    return HttpResponse('<h1><marquee> Hello How are you </h1></marquee>')


def VJ(request):
    return HttpResponse('<h2><marquee>Hi </h2></marquee>')
