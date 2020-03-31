from django.urls import path 

from vcuhunt.landmarks.views import LandmarkCompletedListView, LandmarkUnCompletedListView, LandmarkDetailView

app_name = "landmarks"

urlpatterns = [
    path("~todo/", view=LandmarkUnCompletedListView.as_view(), name="list"), 
    path("~completed/", view=LandmarkCompletedListView.as_view(), name="complete"),
    path("~<int:pk>/", view=LandmarkDetailView.as_view(), name="detail"), 
]