from django.http import HttpResponse

# Create your views here.


def home_view(request):
    return HttpResponse("<h1>Home Page</h1>")


def about_view(request):
    return HttpResponse("<h1>About Page</h1>")


def contact_view(request):
    return HttpResponse("<h1>Contact Page</h1>")
