from django.shortcuts import render
from django.views.generic import ListView, DetailView

from vcuhunt.landmarks.models import Landmark

# Create your views here.
class LandmarkListView(ListView):
    model = Landmark
 
class LandmarkDetailView(DetailView):
    model = Landmark