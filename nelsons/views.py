from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView

from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .models import Nelson
from .serializers import NelsonSerializer

class NelsonListView(ListView):
    model = Nelson
    queryset = Nelson.objects.filter()
    context_object_name = 'nelson_list'
    template_name = 'nelsons/list.html'

class NelsonCreateView(CreateView):
    model = Nelson
    fields = ['name', 'latitude', 'longitude', 'position']
    template_name = 'nelsons/create.html'
    success_url = reverse_lazy('list')

class NelsonDetailView(RetrieveUpdateDestroyAPIView):
	queryset = Nelson.objects.all()
	serializer_class = NelsonSerializer
