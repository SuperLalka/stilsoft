from django.contrib import admin
from django.urls import include, path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions as drf_permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

schema_view = get_schema_view(
   openapi.Info(
      title="Stilsoft solution API",
      default_version='v1',
   ),
   public=True,
   permission_classes=(drf_permissions.AllowAny,),
)

swagger_urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

tokens_url = [
    path('', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('verify/', TokenVerifyView.as_view()),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', include(tokens_url)),
    *swagger_urlpatterns,
    path('', include('transport_routes.urls')),
]
