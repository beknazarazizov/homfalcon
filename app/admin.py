from django.contrib import admin

# Register your models here.
from app.models import Product,ProductAttribute,Attribute,AttributeValue,Image
admin.site.register(Product)
admin.site.register(ProductAttribute)
admin.site.register(Attribute)
admin.site.register(AttributeValue)
admin.site.register(Image)
