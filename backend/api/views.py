import json
from django.shortcuts import render
from django.http import JsonResponse

def greetings(request,*args,**kwargs):
    body   = request.body

    data = {}
    data["headers"] = dict(request.headers)
    
    
    # try:
    #     data =json.loads(body)
    #     print(data)
    # except:
    #     pass

    
    
    print(request.path)
    print(request.content_type)
    print(request.GET)
    print(request.POST)

    # return(JsonResponse({'greet':'hi'}))
    return JsonResponse(data)
    


