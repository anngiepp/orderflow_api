from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='pedidos'
    )

    fecha = models.DateField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)

    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('Enviado', 'Enviado'),
        ('Entregado', 'Entregado'),
    ]

    estado = models.CharField(max_length=20, choices=ESTADOS)

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente.nombre}"