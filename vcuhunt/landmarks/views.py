from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from vcuhunt.landmarks.models import Landmark
# Create your views here.
class LandmarkCompletedListView(ListView):
    model = Landmark

    def get_queryset(self):
        if (self.request.user): 
            return self.request.user.completed_landmark.all()
        return Landmark.objects.all()

class LandmarkUnCompletedListView(ListView):
    model = Landmark

    def get_queryset(self):
        if (self.request.user.is_authenticated): 
            landmarks_list = Landmark.objects.all()
            completed = self.request.user.completed_landmark.all()
            todo = set()
            for landmark in landmarks_list: 
                if landmark not in completed: 
                    todo.add(landmark.id)
            return Landmark.objects.filter(pk__in = todo)
        return Landmark.objects.all()
    
 
class LandmarkDetailView(LoginRequiredMixin, DetailView):
    model = Landmark 