from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions as drf_permissions
from rest_framework.decorators import action

from . import models, permissions, serializers


def index(request, page=None):
    objects = models.Route.objects.all()
    paginator = Paginator(objects, 100)
    page = page if page else 1
    return render(request, 'routes_page.html', context={
        'paginator': paginator.page(page)
    })


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

    @action(methods=('post',), detail=True, permission_classes=[permissions.PassengerPermission])
    def add_review(self, request, id):
        rating = request.data.get('rating', False)
        review_text = request.data.get('review_text', False)
        if not rating and not review_text:
            return HttpResponse('No data available for review')

        review_data = {'rating': rating if rating else None,
                       'review_text': review_text if review_text else None}

        models.PassengersReviews.objects.create(
            user=request.user,
            transport_id=id,
            **review_data
        )
        return HttpResponse('Review added')
