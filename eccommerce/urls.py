from django.contrib import admin
from django.urls import path, include, re_path
from apps.users.views import Login, Logout, UserToken

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from apps.users.views import Login, Logout, UserToken

# Config AWAGGER
schema_view = get_schema_view(
    openapi.Info(
        title="Ecommers API",
        default_version='v 0.1',
        description="API documentation for Ecommers with SWAGGER",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="ismaelrengel100@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # Documentacion con interfaz AWAGGER
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    # Rutes
    path('admin/', admin.site.urls),
    path('', include('apps.users.api.urls')),
    path('refresh-token/',UserToken.as_view(), name='refresh_token'),
    path('logout/', Logout.as_view(), name='logout'),
    path('login/', Login.as_view(), name='login'),
    path('users/', include('apps.users.api.urls')),
    path('products/', include('apps.products.api.routers')),
    path('product-dates/', include('apps.products.api.urls')),
]
