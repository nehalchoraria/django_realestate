from django.shortcuts import render,get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices import bedroom_choices,price_choices,state_choices


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
    listing=get_object_or_404(Listing,pk=listing_id) #model,id
    context={
        'listing':listing,
    }

    return render(request,'listings/listing.html',context)

def search(request):
    query_result=Listing.objects.order_by('-list_date')

    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        if keywords:
            query_result=query_result.filter(description__icontains=keywords) #equivalent to like

    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            query_result=query_result.filter(city__iexact=city)

    if 'state' in request.GET:
        state=request.GET['state']
        if state:
            query_result=query_result.filter(state__iexact=state)

    if 'bedrooms' in request.GET:
        bedrooms=request.GET['bedrooms']
        if bedrooms:
            query_result=query_result.filter(bedrooms__lte=bedrooms) #equivalent to like

    if 'price' in request.GET:
        price=request.GET['price']
        if price:
            query_result=query_result.filter(price__lte=price) #equivalent to like


    paginator=Paginator(query_result,8)
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page)

    context={
    'bedroom_choices':bedroom_choices,
    'price_choices':price_choices,
    'state_choices':state_choices,
    'listings':paged_listings,
    'values':request.GET,
    }
    return render(request,'listings/search.html',context)
