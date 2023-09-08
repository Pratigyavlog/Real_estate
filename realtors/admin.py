from django.contrib import admin

from .models import Realtor

class Realtoritems(admin.ModelAdmin):
    list_display=('id','name','email','phone',)
    list_display_links=('id','name')
    list_per_page=25
    search_fields=('name',)

admin.site.register(Realtor,Realtoritems)
