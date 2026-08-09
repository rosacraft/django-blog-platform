from django.shortcuts import render
from website.models import Contact
from blog.models import Post
from website.forms import ContactForm, NewsletterForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

def index_view(request):
    return render(request, 'website/index.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            
            # Add message to the user 
            messages.add_message(request, messages.SUCCESS, 'Your ticket submitted successfully.')
        else:
            messages.add_message(request, messages.ERROR, 'Your ticket didnt submitted.')
            
    form = ContactForm()
    return render(request, 'website/contact.html', {'form':form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            # back to the main page
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

def about_view(request):
    return render(request, 'website/about.html')

def test_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    
    return render(request, 'test.html', context)
