from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^nelsons/', include('nelsons.urls')),
    url(r'^admin/', admin.site.urls),
]
