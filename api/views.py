from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Product, Category
from api.serializers import ProductSerializer, CategorySerializer, DepthProductSerializer


class ProductList(APIView):

    def get(self, request):
        p = Product.objects.all()
        return Response({'Products': ProductSerializer(p, many=True).data})


class ProductDetail(APIView):

    def get(self, request, id):
        p = get_object_or_404(Product, pk=id)
        return Response({'Product': ProductSerializer(p).data})


class CategoryList(APIView):

    def get(self, request):
        c = Category.objects.all()
        return Response({'Categories': CategorySerializer(c, many=True).data})


class CategoryDetail(APIView):

    def get(self, request, id):
        c = get_object_or_404(Category, pk=id)
        return Response({'Category': CategorySerializer(c).data})


class CategoryProductsDetail(APIView):

    def get(self, request, id):
        p = Product.objects.all().filter(cat_id=id)
        return Response({'Products': DepthProductSerializer(p, many=True).data})