from django.shortcuts import render
from .forms import AppForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage

def index(request):
    if request.method == "POST":
        appform = AppForm(request.POST)
        if appform.is_valid():
            first_name = appform.cleaned_data["first_name"]
            last_name = appform.cleaned_data["last_name"]
            email = appform.cleaned_data["email"]
            date = appform.cleaned_data["date"]
            occupation = appform.cleaned_data["occupation"]
            Form.objects.create(first_name=first_name,last_name=last_name,email=email,date=date,occupation=occupation)

            email_body = f"Job application submitted. Thank You, {first_name}"
            email_message = EmailMessage("Job Application Submission", email_body, to=[email])
            email_message.send()

            messages.success(request, "Form submitted successfully")
    return render(request, "index.html")