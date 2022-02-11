from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext


# Create your views here.

def index(request):
    context_dict = {'boldmessage':'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request,'rango/index.html',context=context_dict)
    

def about(request):
    context = RequestContext(request)
    return render('rango/about.html',{},context)