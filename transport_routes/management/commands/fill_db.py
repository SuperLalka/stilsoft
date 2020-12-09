# -*- coding: utf-8 -*-
import random
from datetime import datetime
from django.core.management.base import BaseCommand

from transport_routes.models import (
    Route, Transport
)
from stilsoft_test import constants


class Command(BaseCommand):

    def handle(self, *args, **options):
        route_objects = Route.objects.count()
        if route_objects < 300:
            while route_objects < 300:
                route, status = Route.objects.get_or_create(number=random.randint(1, 9999),
                                                            route_type=random.choice(constants.TRANSPORT_TYPE_LIST),
                                                            is_active=random.choice([True, False]))
                route_objects += 1

                if status:
                    for num in range(5):
                        transport = Transport.objects.create(vehicle_id_number=random.randint(111111, 999999),
                                                             transport_type=route.route_type)
                        transport.save()
                        route.transports.add(transport)

                        print(datetime.now(), 'transport {0} / {1} for route created'.format(transport.vehicle_id_number,
                                                                                             transport.transport_type))

                print(datetime.now(), 'route {0} / {1} created'.format(route.number, route.route_type))
