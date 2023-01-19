from apps.base.api import GeneralListApiView
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer,IndicatorSerializer,CategoryProductSerializer
from apps.users.authentication_mixin import Authentication

class MeasureUnitListAPIView(Authentication,GeneralListApiView):
    
    serializer_class = MeasureUnitSerializer
    
class IndicatorListAPIView(GeneralListApiView):
    serializer_class = IndicatorSerializer
    
class CategoryProductListAPIView(GeneralListApiView):
    serializer_class = CategoryProductSerializer
    