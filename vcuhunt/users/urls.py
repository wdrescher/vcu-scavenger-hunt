from django.urls import path

from vcuhunt.users.views import (
    user_redirect_view,
    user_update_view,
    user_detail_view,
    UserSuccessfulLandmarkView, 
    UserResetView
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path("~success/<int:landmark>/", view=UserSuccessfulLandmarkView.as_view(), name="success"), 
    path("~reset", view=UserResetView.as_view(), name="reset")
]
