from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView

from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework_jsonp.renderers import JSONPRenderer

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

    def get_success_url(self):
        return reverse_lazy('nelsons:api', kwargs={'pk': self.object.name})

    def get_initial(self):
        return {'name': self.kwargs['name']}


class NelsonDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Nelson.objects.all()
    serializer_class = NelsonSerializer

    renderer_classes = (BrowsableAPIRenderer, JSONPRenderer,)

    def perform_update(self, serializer):
        get_position = self.request.GET.get('position')
        if get_position:
            serializer.save(position=int(get_position))
        else:
            serializer.save()


def check_existence(request):
    name = request.POST.get('name')
    try:
        nelson = Nelson.objects.get(name=name)
        return redirect(reverse_lazy('nelsons:api', kwargs={'pk': nelson.name}))
    except:
        return redirect(reverse_lazy('nelsons:create', kwargs={'name': name}))
