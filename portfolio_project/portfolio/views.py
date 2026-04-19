from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
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
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        # Send email to your Gmail
        try:
            send_mail(
                subject=f"New Contact Message from {name}",
                message=f"Name: {name}\nEmail: {email}\nMessage:\n{message}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            
            # Send auto-reply to user
            send_mail(
                subject="Thanks for contacting me",
                message="I will get back to you soon.",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
            )
        except Exception as e:
            print(f"Email sending failed: {e}")

        return render(request, "contact.html", {
            "success": "Message sent successfully!"
        })

    return render(request, 'contact.html')