from django.shortcuts import render

# Create your views here.
def about_view(request):
    return render(request, 'pages/about.html')

def contact_view(request):
    return render(request, 'pages/contact.html')

def experience_view(request):
    return render(request, 'pages/experience.html')

