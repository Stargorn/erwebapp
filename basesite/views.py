from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm


def home(request):
    return render(request, 'basesite/home.html')

def about(request):
    return render(request, 'basesite/about.html')

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            your_email = form.cleaned_data['your_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, your_email, ['admin@emberruby.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('basesite:success')
    return render(request, "basesite/contact.html", {'form': form})
    
def successView(request):
    return HttpResponse('Success! Thank you for your message.')
