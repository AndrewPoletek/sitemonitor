from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    template = 'main/index.html'
    #return HttpResponse('Hello World')
    return render(request, template)
