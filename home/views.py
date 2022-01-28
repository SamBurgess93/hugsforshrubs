from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from products.models import Product

# Create your views here.

def index(request):
    """ A view to return the index page """
    
    return render(request, 'home/index.html')

