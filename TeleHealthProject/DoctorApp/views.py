from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {}
    context['message'] = 'hello world'
    return HttpResponse(render(request, 'DoctorApp/index.html', context))
