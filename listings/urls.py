from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path('', views.listing_list),
    path('listings/<pk>', views.listing_retrieve),
    path('listings/<pk>/edit', views.listing_update),
    path('add-listing', views.listing_create),
    path('listings/<pk>/delete', views.listing_delete),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)