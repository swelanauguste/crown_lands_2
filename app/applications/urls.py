from django.urls import path
from . import views

app_name = "applications"
urlpatterns = [
    path(
        "",
        views.IndividualApplicationList.as_view(),
        name="individual-list",
    ),
    path(
        "individual/create",
        views.IndividualApplicationCreate.as_view(),
        name="individual-create",
    ),
    path(
        "individual/detail/<int:pk>",
        views.IndividualApplicationDetail.as_view(),
        name="individual-detail",
    ),
    path(
        "individual/update/<int:pk>",
        views.IndividualApplicationUpdate.as_view(),
        name="individual-update",
    ),
]
