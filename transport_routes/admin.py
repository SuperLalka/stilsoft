from django.contrib import admin

from transport_routes.models import (
    Route, Transport, User
)


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('number', 'route_type')
    list_filter = ('route_type',)
    list_per_page = 30


@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    list_display = ('vehicle_id_number', 'transport_type')
    list_filter = ('transport_type',)
    search_fields = ['vehicle_id_number']
    list_per_page = 50


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'user_group', 'is_active', 'is_staff')
    list_filter = ('user_group', 'is_staff')
    list_per_page = 20
