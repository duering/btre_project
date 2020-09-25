from django.shortcuts import render
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger

from.models import Listing

def index(request):
    listings = Listing.objects.all()

    paginator = Paginator(listings, 6)
    page_number = request.GET.get('page')
    paged_listings = paginator.get_page(page_number)
    
    return render(request, 'listings/listings.html', {
        'listings': paged_listings
    })

def listing(request, listing_id):
    listing = Listing.objects.all().get(id=listing_id)
    return render(request, 'listings/listing.html', {
        'listing': listing
    })

def search(request):
    return render(request, 'listings/search.html')
