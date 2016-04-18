from django.conf.urls import url

from .views import NelsonListView, NelsonCreateView, NelsonDetailView, check_existence

urlpatterns = [
    url(r'^$', NelsonListView.as_view(), name='list'),
    url(r'^create/?(?P<name>[-\w\d]*)/$', NelsonCreateView.as_view(), name='create'),
    url(r'^check/$', check_existence, name='check'),
    url(r'^(?P<pk>[-\w\d]+)/$', NelsonDetailView.as_view(), name='api'),
]
