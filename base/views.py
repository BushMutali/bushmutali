from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'base/index.html')

def about_page(request):
    return render(request, 'base/about.html')

def profile_page(request):
    return render(request, 'base/profile.html')