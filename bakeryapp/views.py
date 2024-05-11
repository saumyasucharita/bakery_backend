from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    """
    API endpoint that allows to get all bakery products
    """
    @api_view(['GET'])
    def getProductList(self, request):
        products = Product.objects.all().order_by('product_id')
        serializer = ProductSerializer(products, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    """
    API endpoint that allows to get the product details by its product_id
    """
    @api_view(['GET'])
    def getProductbyId(self, request, req_product_id):
        try:
            product = Product.objects.get(product_id=req_product_id)
        except Product.DoesNotExist:
            return Response({"message": "Product id not found in the database"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, many=False)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
    
    """
    API endpoint that allows to add product details 
    """
    @api_view(['POST'])
    def addProduct(self, request):
        serializer = ProductSerializer(data = request.data)
      
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
        
        else:
            errors = serializer.errors
            return Response({"errors": errors}, status=status.HTTP_400_BAD_REQUEST)
        
    """
    API endpoint that allows to update a product
    """
    @api_view(['PUT'])
    def updateProduct(self, request, pk):
        product = Product.objects.get(product_id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
    
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    """
    API endpoint that allows to delete a product
    """
    @api_view(['DELETE'])
    def deleteProduct(self, pk):
        product = Product.objects.get(product_id=pk)
        product.delete()
    
        return Response({"status": "success", "data": "Item Deleted"})