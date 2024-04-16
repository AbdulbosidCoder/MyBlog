from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permitions import IsOwnerOrReadOnly
from drf_yasg.generators import OpenAPISchemaGenerator


class JWTSchemaGenerator(OpenAPISchemaGenerator):
    def get_security_definitions(self):
        return {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "JWT token obtained from authentication endpoint"
            }
        }



schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="parpiyev.abdulbosid@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[AllowAny],
    generator_class=JWTSchemaGenerator,
)

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
