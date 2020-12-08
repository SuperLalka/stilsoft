from django.conf.urls import url
from django.urls import include

from rest_framework.routers import DefaultRouter
from . import views


routerAPI = DefaultRouter()
routerAPI.register(r'routes', views.RouteViewSet, basename='routes')
routerAPI.register(r'transports', views.TransportViewSet, basename='transports')


app_name = 'transport_routes'
urlpatterns = [
    url(r'^api/', include(routerAPI.urls)),
    url(r'^(?P<page>\d+)?', views.index, name='index'),
]
