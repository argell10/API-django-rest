from django.contrib import admin
from apps.products.models import Product,CategoryProduct,Indicator,MeasureUnit

admin.site.register(Product),
admin.site.register(CategoryProduct),
admin.site.register(Indicator),
admin.site.register(MeasureUnit),
