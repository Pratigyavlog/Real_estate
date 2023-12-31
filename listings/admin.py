from django.contrib import admin

from .models import Listing

class ListingItems(admin.ModelAdmin):
    list_display=('id', 'title', 'price', 'is_published', 'realtor')
    list_display_links=('id', 'title')
    list_filter=('realtor',)
    list_editable=('is_published',)
    search_fields=('title', 'description', 'address', 'city', 'state', 'zipcode', 'price',)
    list_per_page=25

admin.site.register(Listing,ListingItems)
