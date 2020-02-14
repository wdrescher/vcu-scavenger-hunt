from django.urls import path 

from vcuhunt.landmarks.views import LandmarkListView, LandmarkDetailView

app_name = "landmarks"

urlpatterns = [
    path("~view/", view=LandmarkListView.as_view(), name="list"), 
    path("~<int:pk>/", view=LandmarkDetailView.as_view(), name="detail"), 
]