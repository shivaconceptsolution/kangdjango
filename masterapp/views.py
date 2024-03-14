from django.shortcuts import render

def home(request):
    return render(request,"masterapp/home.html")
def aboutus(request):
    return render(request,"masterapp/about.html")