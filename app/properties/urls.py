from django.urls import path

from . import views


app_name = "properties"


urlpatterns = [
    path("", views.PropertyListView.as_view(), name="property-list"),
    path(
        "detail/<int:pk>/", views.PropertyDetailView.as_view(), name="property-detail"
    ),
    path("create/", views.PropertyCreateView.as_view(), name="property-create"),
    path(
        "update/<int:pk>/", views.PropertyUpdateView.as_view(), name="property-update"
    ),
]
