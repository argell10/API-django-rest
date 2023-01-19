from apps.products.models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('state','created_date','modified_date','delete_date')
        
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'image': instance.image if instance.image != '' else '',
            'description': instance.description,
            'measure_unit': instance.measure_unit.description if instance.measure_unit is not None else '',
            'category_product': instance.category_product.description if instance.category_product is not None else ''
        }