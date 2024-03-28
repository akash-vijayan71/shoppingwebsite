from django.contrib import admin
from . models import Contact
from . models import Register,Product,Cart,Order,Adminlogin,Category,Wishlist

# Register your models here.

admin.site.register(Contact) 
admin.site.register(Register)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Adminlogin)
admin.site.register(Category)
admin.site.register(Wishlist)


