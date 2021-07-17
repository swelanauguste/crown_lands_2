from django.urls import path

from . import views

app_name = "clients"

urlpatterns = [
    path("individuals", views.IndividualList.as_view(), name="individual-list"),
    path(
        "individual/detail/<int:pk>",
        views.AddIdentification.as_view(),
        name="individual-detail",
    ),
    path(
        "individual/update/<int:pk>",
        views.IndividualUpdate.as_view(),
        name="individual-update",
    ),
    path(
        "individual/create",
        views.IndividualCreate.as_view(),
        name="individual-create",
    ),
    # ==============================
    path(
        "identifications",
        views.IdentificationList.as_view(),
        name="identification-list",
    ),
    path(
        "identification/detail/<int:pk>",
        views.IdentificationDetail.as_view(),
        name="identification-detail",
    ),
    path(
        "identification/update/<int:pk>",
        views.IdentificationUpdate.as_view(),
        name="identification-update",
    ),
    path(
        "identification/create",
        views.IdentificationCreate.as_view(),
        name="identification-create",
    ),
]
