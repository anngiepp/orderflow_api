from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from .models import Cliente, Pedido
from .serializers import ClienteSerializer, PedidoSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    filter_backends = [SearchFilter]

    search_fields = [
        'estado',
        'cliente__nombre'
    ]