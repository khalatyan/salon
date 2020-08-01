from django.contrib import admin
from .models import Types, Brands, Products
admin.autodiscover()

admin.site.register(Types)
admin.site.register(Brands)
#admin.site.register(Products)


class ProductAdmin(admin.ModelAdmin):
    model = Products
    list_display = ['product_type', 'number', 'volume_sp', 'volume_rp', 'volume']
    #Filtering on side - for some reason, this works
    #list_filter = ['title', 'author__name']


admin.site.register(Products, ProductAdmin)


