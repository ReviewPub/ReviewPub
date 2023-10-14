from django.contrib import admin
from django.urls import path

from review_pub.swagger import schema_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger-ui/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
]
