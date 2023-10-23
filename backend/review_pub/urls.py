from django.urls import include, path
from rest_framework import routers

from .views import DomainViewSet, LanguageViewSet, PaperViewSet, ReviewViewSet, UserViewSet


app_name = 'review_pub'

router = routers.DefaultRouter()
router.register('domains', DomainViewSet)
router.register('languages', LanguageViewSet)
router.register('papers', PaperViewSet)
router.register('reviews', ReviewViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]