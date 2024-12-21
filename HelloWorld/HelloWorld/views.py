from django.http import HttpResponse

# Create your views here.
def hello(request):
    if(request.method=='GET'):
        return HttpResponse("<h1>Hello World </h1>")
    else:
        return HttpResponse("<h1>Sorry! This page is not found</h1>")
