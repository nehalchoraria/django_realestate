from django.shortcuts import render
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def index(request):
    listings=Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator=Paginator(listings,2)
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page)

    content = {
    'listings':paged_listings
    }

    return render(request,'listings/listings.html',content)

def listing(request,listing_id):
    return render(request,'listings/listing.html')

def search(request,listing_id):
    return render(request,'listings/search.html')
