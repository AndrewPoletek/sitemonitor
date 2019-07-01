from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    template = 'main/index.html'
    #return HttpResponse('Hello World')
    return render(request, template)

def addWebsite(request):
    if request.method == 'POST':
        website_address = request.POST['web_address']
        time_interval = int(request.POST['interval_time'])
        verify_string = request.POST['verify_string']
        print(website_address)
        print(verify_string)
        print(time_interval)
    template = 'main/addWebsite.html'
    return render(request, template)
