from rest_framework import viewsets, status
from rest_framework.response import Response
from apps.users.authentication_mixin import Authentication
from apps.products.api.serializers.product_serializers import ProductSerializer

class ProductViewSet(Authentication,viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    # queryset = ProductSerializer.Meta.model.objects.filter(state=True)
    def get_queryset(self, pk=None):
        """ Devuelve el detalle del producto con el id del producto que se ingrese """
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(state=True, id=pk).first()
    
    #Al ifual que con las APIView tambien podemos redefinir los metodos dentro de ModelViewset
    #Get
    def list(self, request):
        """ 
        Devuleve Los productos existentes
        
        
        Retorna los productos que existan o aquellos que tengan su state en True """
        product_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(product_serializer.data,status = status.HTTP_200_OK)
    #Post
    def create(self, request):
        """ Crea productos por medio del metodo post """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Product created successfully.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Update
    def update(self, request, pk=None):
        """ Actualiza los valores que se haya espeificado en el detalle de un producto con id espesifico """
        if self.get_serializer(pk):
            product_serializer = self.serializer_class(
                self.get_queryset(pk), data=request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status=status.HTTP_200_OK)
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Destroy
    def destroy(self, request, pk=None):
        """ Marca como false el state del producto por medio del id """
        product = self.get_queryset(pk)
        if product:
            product.state = False
            product.save()
            return Response({'message': 'Product deleted successfully.'}, status=status.HTTP_200_OK)
        return Response({'message': 'Product not found.'}, status=status.HTTP_400_BAD_REQUEST)

