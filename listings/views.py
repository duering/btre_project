from django.shortcuts import render

from.models import Listing

def index(request):
    listings = Listing.objects.all
    return render(request, 'listings/listings.html', {
        'listings': listings
    })

def listing(request, listing_id):
    listing = Listing.objects.all().get(id=listing_id)
    return render(request, 'listings/listing.html', {
        'listing': listing
    })

def search(request):
    return render(request, 'listings/search.html')
