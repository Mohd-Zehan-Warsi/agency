from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

from .models import ContactMessage


def contact_submit(request):

    if request.method != "POST":
        return redirect("/#contact")

    name = request.POST.get("name", "").strip()
    email = request.POST.get("email", "").strip()
    phone = request.POST.get("phone", "").strip()
    subject = request.POST.get("subject", "").strip()
    message = request.POST.get("message", "").strip()

    # Required fields
    if not name or not email or not message:
        messages.error(
            request,
            "Please fill in your name, email and message."
        )
        return redirect("/#contact")

    # Save user query
    ContactMessage.objects.create(
        name=name,
        email=email,
        phone=phone,
        subject=subject,
        message=message,
    )

    messages.success(
        request,
        "Thank you! Your message has been sent successfully."
    )

    return redirect("/#contact")
# Create your views here.
from django.contrib import messages
from django.shortcuts import redirect


def submit(request):
    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # फिलहाल testing
        print("NAME:", name)
        print("EMAIL:", email)
        print("PHONE:", phone)
        print("SUBJECT:", subject)
        print("MESSAGE:", message)

        messages.success(
            request,
            "Your message has been sent successfully."
        )

    return redirect("/#contact")
