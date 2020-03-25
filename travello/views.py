from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
     
     demolist = Destination.objects.all()
     return render(request,'index.html',{"demolist":demolist})