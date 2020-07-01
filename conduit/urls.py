from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('conduit.apps.authentication.urls', namespace='authentication')),
    path('api/', include('conduit.apps.profiles.urls', namespace='profiles')),
    path('api/', include('conduit.apps.articles.urls', namespace='articles')),
]
