from django.shortcuts import render, HttpResponse
from .models import websites, connection_log

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
        newConnection_log = connection_log()
        newConnection_log.website_address = website_address
        newConnection_log.status = 1
        newConnection_log.response_Time = 1
        newConnection_log.checked = 1
        newConnection_log.datetime_check = '1800-01-01 00:00'
        newConnection_log.save()
        added = True
    template = 'main/addWebsite.html'
    return render(request, template, {'added' : added})

def checkWebsites(request):
    template = 'main/checkWebsites.html'
    allWebsites = websites.objects.all()
    print(allWebsites)
    return render(request, template, {'allWebsites' : allWebsites})

def statusWebsites(request, id):
    #print("STATUS: "+str(id))
    website = websites.objects.get(id=id)
    lastStatus = connection_log.objects.filter(website_address=website.website_address).order_by('-id')
    if str(lastStatus[0].status).find('<Response') >= 0 :
        response = "OK [200]"
    else:
        response = lastStatus[0].status

    print(lastStatus[0].status.find('<Response'))
    return HttpResponse(str(response))