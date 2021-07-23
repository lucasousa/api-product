from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from core.api.viewsets import ProductViewSet
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register('products', ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )