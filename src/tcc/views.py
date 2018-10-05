from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import ContactForm

def home(request):
    context = {
        "content":"Homepage"
    }
    return render(request, 'home.html', context)

def about(request):
    context ={
        "title":"About us",
    }
    return render(request, 'about/view.html', context)

def contact(request):
    contact_form = ContactForm(request.POST or None)
    context ={
        "title":"Contact Page",
        "form": contact_form,
    }
    if contact_form.is_valid():
        name = contact_form.cleaned_data.get('name')
        email = contact_form.cleaned_data.get('email')
        message = contact_form.cleaned_data.get('content')
        subject = contact_form.cleaned_data.get('subject')
        from_email = email

        content = (("\nFrom: " + email+
                    "Subject: " + subject +
                    "Name: " + name +
                    +"\n" + message))

        send_mail(subject, content, from_email, ['lesprojeto@gmail.com'])

        print(contact_form.cleaned_data)
    return render(request, "contact/view.html", context)

def exam(request):
    return render(request, 'exam.html', {})
