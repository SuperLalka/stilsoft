from django.db import models
from django.contrib.auth.models import AbstractUser

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
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{0} / {1}'.format(self.route_type, self.number)

    def get_route_transports(self):
        return self.transports.all()

    class Meta:
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'


class Transport(models.Model):
    vehicle_id_number = models.PositiveIntegerField(default=None,
                                                    help_text=TRANSPORT_NUMBER,
                                                    null=True, blank=True)
    description = models.CharField(max_length=100, help_text="Enter a description of the transport",
                                   null=True, blank=True)
    transport_type = models.CharField(max_length=5, choices=constants.TRANSPORT_TYPE,
                                      help_text=TRANSPORT_TYPE, default='bus')

    def __str__(self):
        return '{0} / {1}'.format(self.transport_type, self.vehicle_id_number)

    class Meta:
        verbose_name = 'Transport'
        verbose_name_plural = 'Transports'


class User(AbstractUser):
    user_group = models.CharField(max_length=10, choices=constants.USER_GROUP,
                                  help_text='Select user group', default='Passenger')
    reviews = models.ManyToManyField('Transport', through='PassengersReviews')

    def check_group(self, group):
        return group == self.user_group


class PassengersReviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE)
    rating = models.CharField(max_length=10, choices=constants.SELECT_RATING,
                              help_text='Select user group', null=True, blank=True)
    review_text = models.CharField(max_length=100, help_text="Enter your review text",
                                   null=True, blank=True)

    class Meta:
        db_table = "transport_routes_passengers_reviews"
