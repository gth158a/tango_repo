from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hello world!. <a href=\"/rango/about/\">about</a>.")

def about(request):
    return HttpResponse("Here is the about page. <a href=\"/rango/\">Index</a>.")