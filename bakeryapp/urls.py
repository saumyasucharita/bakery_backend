from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

schema_view = swagger_get_schema_view(
    openapi.Info(
        title = "Bakery API",
        default_version = '1.0.0',
        description = "API documentation of App",
    ),
    public=True,
)

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('v1/', include(router.urls)),  # Include router URLs
    path('v1/docs/', schema_view.with_ui('swagger', cache_timeout=0)),
] 
