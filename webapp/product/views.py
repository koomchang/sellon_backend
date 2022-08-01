from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from product.permissions import IsProductEditableOrDestroyable
from .models import Product, ProductCategory, ProductGroup
from .serializers import ProductSerializer, ProductCategorySerializer, ProductGroupSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsProductEditableOrDestroyable,
    ]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class ProductCategoryListAPIView(ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    pagination_class = None


class ProductGroupsListAPIView(ListAPIView):
    queryset = ProductGroup.objects.all()
    serializer_class = ProductGroupSerializer
    pagination_class = None
