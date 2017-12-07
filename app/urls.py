from django.conf.urls import url

from .views import RetrieveOptions


urlpatterns = [
    url(r'^retrieve_options/$', RetrieveOptions, name='retrieve_options'),
]
