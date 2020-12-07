from rest_framework import viewsets, mixins
from rest_framework import permissions as drf_permissions
from rest_framework.viewsets import GenericViewSet

from . import models, permissions, serializers


class RouteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RouteSerializer
    queryset = models.Route.objects.all()
    filterset_fields = ['route_type', 'is_active']
    ordering_fields = ['number', 'route_type', 'is_active']
    lookup_field = 'id'

    permission_classes = [drf_permissions.IsAuthenticated]
    permission_classes_by_action = {
        'create': [permissions.AdminPermission],
        'retrieve': [drf_permissions.IsAuthenticated],
        'list': [drf_permissions.IsAuthenticated],
        'update': [permissions.AdminPermission],
        'partial_update': [permissions.AdminPermission],
        'destroy': [permissions.AdminPermission]
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class TransportViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TransportSerializer
    queryset = models.Transport.objects.all()
    filterset_fields = ['transport_type']
    ordering_fields = ['vehicle_id_number', 'transport_type']
    lookup_field = 'id'

    permission_classes = [drf_permissions.IsAuthenticated]
    permission_classes_by_action = {
        'create': [permissions.AdminPermission],
        'retrieve': [drf_permissions.IsAuthenticated],
        'list': [drf_permissions.IsAuthenticated],
        'update': [permissions.AdminPermission | permissions.DriverPermission],
        'partial_update': [permissions.AdminPermission | permissions.DriverPermission],
        'destroy': [permissions.AdminPermission]
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
