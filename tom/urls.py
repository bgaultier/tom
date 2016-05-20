from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView

from . import views
from hits import views as hits_views

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='list'), name='home'),
    url(r'^nelsons/', include('nelsons.urls', namespace='nelsons')),
    url(r'^admin/', admin.site.urls),
    url(r'^hits', hits_views.index),
]
