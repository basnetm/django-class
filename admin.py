from django.contrib import admin
from . models import product,contacts
# Register your models here aftr filing content in models so,dont forget to do this.

# class productAdmin(admin.ModelAdmin):
#     list_display=('product_name','category','subcategory','price','image')
admin.site.register(product)

admin.site.register(contacts)

