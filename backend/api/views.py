from django.shortcuts import render
from django.http import JsonResponse

def greetings(request,*args,**kwargs):
    return(JsonResponse({'greet':'hi'}))


