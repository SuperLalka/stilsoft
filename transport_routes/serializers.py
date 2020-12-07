from rest_framework import serializers

from . import models


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Route
        fields = ['id', 'number', 'route_type', 'is_active']

    def validate_route_type(self, value):
        raise serializers.ValidationError(
            "Changing the route type is prohibited")

    def validate_is_active(self, value):
        if not isinstance(value, bool):
            raise serializers.ValidationError(
                "incorrect route status")
        return value


class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transport
        fields = ['id', 'vehicle_id_number', 'transport_type', 'description']

    def validate_vehicle_id_number(self, value):
        if self.context['request'].user.user_group == 'driver':
            raise serializers.ValidationError(
                "The driver can change the vehicle identification number")
        return value

    def validate_transport_type(self, value):
        raise serializers.ValidationError(
            "Changing the type of vehicle is prohibited")


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'user_group']
