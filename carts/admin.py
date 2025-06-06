from django.contrib import admin
from .models import Cart, CartItem
# Register your models here.

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart','product','quantity','is_active')
    
class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id','date_added')

admin.site.register(Cart,CartAdmin)
admin.site.register(CartItem,CartItemAdmin)
