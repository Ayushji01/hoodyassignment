from django.shortcuts import render
from .models import roomdesc


# Create your views here.
def index(request):
    
     rooms = roomdesc.objects.all()


     return render(request, "index.html", {'rooms': rooms})



    