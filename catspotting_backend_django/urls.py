from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        path('admin/', admin.site.urls),
        path('', include('catspotting_backend.urls')),
        path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        path('api/token/obtain/', TokenObtainPairView.as_view(),
             name='token_obtain_pair'),
        path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]
