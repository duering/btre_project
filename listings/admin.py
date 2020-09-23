from django.contrib import admin

from .models import Listing

import locale
locale.setlocale(locale.LC_ALL, '')

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'formatted_price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor', )
    list_editable = ('is_published', )
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25

    def formatted_price(self, obj):
        # obj is the Model instance
        return '{:,.2f}'.format(obj.price)
        
admin.site.register(Listing, ListingAdmin)

