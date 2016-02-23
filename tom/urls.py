from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='nelson-list'), name='home'),
    url(r'^nelsons/', include('nelsons.urls', namespace='nelsons')),
    url(r'^admin/', admin.site.urls),
]
