from django.conf.urls import url, include
from django.contrib import admin

from .views import NelsonListView, NelsonCreateView, NelsonDetailView

urlpatterns = [
    url(r'^$', NelsonListView.as_view(), name='list'),
    url(r'^create/$', NelsonCreateView.as_view(), name='create'),
    url(r'^(?P<pk>[-\w\d]+)/$', NelsonDetailView.as_view(), name='api'),
]
