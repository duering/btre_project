from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger

from .choices import price_choices, bedroom_choices, state_choices
from.models import Listing

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page_number = request.GET.get('page')
    paged_listings = paginator.get_page(page_number)
    
    return render(request, 'listings/listings.html', {
        'listings': paged_listings
    })

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    return render(request, 'listings/listing.html', {
        'listing': listing
    })

def search(request):
    # 'parameters': {
    #         'keywords': request.GET.get('keywords'),
    #         'city': request.GET.get('city'),
    #         'state': request.GET.get('state'),
    #         'price': request.GET.get('price'),
    #         'bedrooms': request.GET.get('bedrooms'),
    #     },

    queryset_list = Listing.objects.order_by('-list_date').filter(is_published=True)
    
    # Keywords
    keywords = request.GET.get('keywords')
    if keywords:
        queryset_list = queryset_list.filter(description__icontains=keywords) #contains text
    
    # City
    city = request.GET.get('city')
    if city:
        queryset_list = queryset_list.filter(city__iexact=city) #case insensitive
 
    # State
    state = request.GET.get('state')
    if state:
        queryset_list = queryset_list.filter(state__iexact=state) #case insensitive

    # Bedrooms
    bedrooms = request.GET.get('bedrooms')
    if bedrooms:
        queryset_list = queryset_list.filter(bedrooms__lte=bedrooms) #less or equal to

    # Price
    price = request.GET.get('price')
    if price:
        queryset_list = queryset_list.filter(price__lte=price) #less or equal to


    context = {
        'listings': queryset_list,
        'values': request.GET,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices
    }
    return render(request, 'listings/search.html', context)
