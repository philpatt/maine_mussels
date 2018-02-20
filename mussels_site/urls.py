from django.conf.urls import url
from mussels_site import views


urlpatterns = [
    url(r'^$', views.index, name='index')
]