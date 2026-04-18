from django.shortcuts import render
from .models import ContactMessage

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def soilguard(request):
    return render(request, 'projects/soilguard.html')

def finance(request):
    return render(request, 'projects/finance.html')

def experience(request):
    return render(request, 'experience.html')

def experience_detail(request):
    return render(request, 'experience_detail.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def contact(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            message=request.POST.get("message")
        )

        return render(request, "contact.html", {
            "success": "Message sent successfully!"
        })

    return render(request, 'contact.html')