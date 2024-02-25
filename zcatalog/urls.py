from zcatalog.apps import ZcatalogConfig
from django.urls import path

from zcatalog.views import HomeView, ContactsView

app_name = ZcatalogConfig

urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('contacts/', ContactsView.as_view(), name='contact')
]