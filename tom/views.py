from django.http import HttpResponse

def home(request):
    return HttpResponse("Il n'y a rien ici ! Par contre, allez jeter un coup d'oeil sur la section Nelson et Tom du MOOC :)", content_type="text/plain")
