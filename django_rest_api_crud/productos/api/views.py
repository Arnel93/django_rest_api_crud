from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny

from ..models import Producto
from .serializers import ProductoSerializer

from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .pagination import CustomPagination
from django_filters import rest_framework as filters
from .filters import ProductoFilter

class ListCreateProductoAPIView(ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = (IsAuthenticated,)
    
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductoFilter

    
class RetrieveUpdateDestroyProductoAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = (IsAuthenticated,)




