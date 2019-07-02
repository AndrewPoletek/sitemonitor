from django.shortcuts import render, HttpResponse
from .models import websites

# Create your views here.

def index(request):
    template = 'main/index.html'
    #return HttpResponse('Hello World')
    return render(request, template)

def addWebsite(request):
    added = False
    if request.method == 'POST':
        website_address = request.POST['web_address']
        time_interval = int(request.POST['interval_time'])
        verify_string = request.POST['verify_string']
        newWebsite = websites()
        newWebsite.website_address = website_address
        newWebsite.verify_string = verify_string
        newWebsite.time_interval = time_interval
        newWebsite.save()
        added = True
    template = 'main/addWebsite.html'
    return render(request, template, {'added' : added})

def checkWebsites(request):
    template = 'main/checkWebsites.html'
    allWebsites = websites.objects.all()
    print(allWebsites)
    return render(request, template, {'allWebsites' : allWebsites})