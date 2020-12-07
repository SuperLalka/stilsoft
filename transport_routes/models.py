from django.db import models

from stilsoft_test import constants

ROUTE_TYPE = "Select the type of transport route"
TRANSPORT_TYPE = "Select the type of transport"
TRANSPORT_NUMBER = "Enter the board number of the vehicle"


class Route(models.Model):
    number = models.PositiveSmallIntegerField(default=None,
                                              help_text="Enter route number")
    transports = models.ManyToManyField('Transport')
    route_type = models.CharField(max_length=5, choices=constants.TRANSPORT_TYPE,
                                  help_text=ROUTE_TYPE, default='bus')

    def __str__(self):
        return '{0} / {1}'.format(self.route_type, self.number)

    class Meta:
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'


class Transport(models.Model):
    board_number = models.PositiveIntegerField(default=None,
                                               help_text=TRANSPORT_NUMBER,
                                               null=True, blank=True)
    transport_type = models.CharField(max_length=5, choices=constants.TRANSPORT_TYPE,
                                      help_text=TRANSPORT_TYPE, default='bus')

    def __str__(self):
        return '{0} / {1}'.format(self.transport_type, self.board_number)

    class Meta:
        verbose_name = 'Transport'
        verbose_name_plural = 'Transports'
