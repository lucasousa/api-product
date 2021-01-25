from rest_framework.viewsets import ModelViewSet
from core.models import Product
from .serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        id_product = self.request.query_params.get('id', None)

        if id_product:
            queryset = Product.objects.filter(id=id_product)
        return queryset
