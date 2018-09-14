from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm

def home(request):
    context = {
        "content":"Homepage"
    }
    return render(request, 'home.html', context)

def about(requet):
    return render(request, 'about.html', {})

def contact(request):
    contact_form = ContactForm(request.POST or None)
    context ={
        "title":"Contact Page",
        "content":"Welcome to the contact page.",
        "form": contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact/view.html", context)

def exam(request):
    return render(request, 'exam.html', {})
