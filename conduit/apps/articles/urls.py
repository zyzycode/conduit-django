from django.conf.urls import include, url
from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import ArticleViewSet

app_name = 'articles'

router = DefaultRouter(trailing_slash=False)
router.register(r'articles', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
