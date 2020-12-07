from django.contrib import admin

from transport_routes.models import (
    Route, Transport
)


@admin.register(Route)
class SubPagesArticleAdmin(admin.ModelAdmin):
    list_display = ('number', 'route_type')
    list_filter = ('route_type',)
    list_per_page = 30


@admin.register(Transport)
class SubPagesSectionAdmin(admin.ModelAdmin):
    list_display = ('board_number', 'transport_type')
    list_filter = ('transport_type',)
    search_fields = ['board_number']
    list_per_page = 50
