from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from .models import Contact

# Create your views here.
def contact(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        realtor_email = request.POST.get('realtor_email')
        listing_id = request.POST.get('listing_id')
        listing = request.POST.get('listing')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        # Check if user has made inquiry already
        has_contacted = Contact.objects.filter(user_id=user_id, listing_id=listing_id).exists()
        if has_contacted:
            messages.error(request, 'You have already submitted a request on this listing.')
            return redirect('/listings/' + listing_id)

        contact = Contact.objects.create(
            listing = listing,
            listing_id = listing_id,
            name = name,
            email = email,
            phone = phone,
            message = message,
            user_id = user_id,            
        )
        contact.save()
        send_mail(
            'Property Listing Inquiry',
            'There has been an Inquiry for {}. Sign into admin panel for more info.'.format(listing),
            'info',
            ['ohadduering@gmail.com'],
            fail_silently=False,
        )
        
        messages.success(request, "A request has been submitted, a realtor will get back to you soon.")
        return redirect('/listings/' + listing_id)