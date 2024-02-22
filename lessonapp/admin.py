from django.contrib import admin
from .models import Product, User, Order


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address', 'date_birth')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('date_birth',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name_product', 'description_product', 'formatted_price', 'number_product', 'date_addition')
    search_fields = ('name_product', 'description_product')
    list_filter = ('date_addition',)

    def formatted_price(self, obj):
        return '${:.2f}'.format(obj.price_product)
    formatted_price.short_description = 'Price'


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'get_products', 'general_sum', 'formation_date')
    list_filter = ('formation_date',)
    search_fields = ('customer__name',)
    readonly_fields = ['formation_date']

    def get_products(self, obj):
        return ", ".join([p.name_product for p in obj.products.all()])
    get_products.short_description = 'Products'


admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
