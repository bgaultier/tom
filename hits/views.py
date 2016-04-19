from django.http import HttpResponse
from .models import Hit

def index(request):
    hit = Hit()
    hit.save()
    hits = Hit.objects.count()
    return HttpResponse(hits, content_type="text/plain")
