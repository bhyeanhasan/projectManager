from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Project Management Tool API",
        default_version='v1',
        description="API documentation for managing users, projects, tasks, and comments",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@techforing.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('mainApp.urls')),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('admin/', admin.site.urls),

]
