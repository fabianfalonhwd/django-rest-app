from django.conf.urls import include, url
from rest_framework import routers
from .viewsets import SerieViewSet
router = routers.DefaultRouter()
router.register(r'series', SerieViewSet)
urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    url(r'^', include(router.urls)),
]
