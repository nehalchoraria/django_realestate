from django.shortcuts import render
from .models import Listing

def index(request):
    listings=Listing.objects.all()
    content = {
    'listings':listings
    }

    return render(request,'listings/listings.html',content)

def listing(request,listing_id):
    return render(request,'listings/listing.html')

def search(request,listing_id):
    return render(request,'listings/search.html')
