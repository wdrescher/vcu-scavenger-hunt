from django.shortcuts import render
from django.views.generic import ListView, DetailView

from vcuhunt.landmarks.models import Landmark

# Create your views here.
class LandmarkCompletedListView(ListView):
    model = Landmark

    def get_queryset(self):
        return self.request.user.completed_landmark.all()

class LandmarkUnCompletedListView(ListView):
    model = Landmark

    def get_queryset(self):
        landmarks_list = Landmark.objects.all()
        completed = self.request.user.completed_landmark.all()
        todo = set()
        for landmark in landmarks_list: 
            if landmark not in completed: 
                todo.add(landmark.id)
        return Landmark.objects.filter(pk__in = todo)
    
 
class LandmarkDetailView(DetailView):
    model = Landmark 