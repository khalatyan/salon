from django.contrib import admin
from .models import ReceiveProducts, SpentProducts
from Products.models import Products
from django.contrib import admin

#admin.site.register(ReceiveProducts)
#admin.site.register(SpentProducts)


class SaveDataRP(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        product = Products.objects.filter(product_type = obj.product_type)
        product = product.filter(number = obj.number)
        if (len(product) == 0):
            new_product = Products(
                product_type=obj.product_type,
                number=obj.number,
                volume_sp=0,
                volume_rp=obj.volume * obj.quantity,
                volume=obj.volume * obj.quantity
            )
            new_product.save()
        else:
            product = product[0]
            product.volume_rp = product.volume_rp + obj.volume * obj.quantity
            product.volume = product.volume_rp - product.volume_sp
            product.save()

        super().save_model(request, obj, form, change)

admin.site.register(ReceiveProducts, SaveDataRP)

class SaveDataSP(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        product = Products.objects.filter(product_type = obj.product_type)
        product = product.filter(number = obj.number)

        if (len(product) == 0):
            new_product = Products(
                product_type=obj.product_type,
                number=obj.number,
                volume_sp=obj.volume,
                volume_rp=obj.volume,
                volume=0
            )
            new_product.save()
        else:
            product = product[0]
            product.volume_sp = product.volume_sp + obj.volume
            product.volume = product.volume_rp - product.volume_sp
            product.save()

        super().save_model(request, obj, form, change)

admin.site.register(SpentProducts, SaveDataSP)
