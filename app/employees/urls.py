from django.urls import path
from . import views

app_name = "employees"


urlpatterns = [
    path("", views.EmployeeListView.as_view(), name="employee-list"),
    path(
        "detail/<int:pk>/", views.EmployeeDetailView.as_view(), name="employee-detail"
    ),
    path(
        "update/<int:pk>/", views.EmployeeUpdateView.as_view(), name="employee-update"
    ),
]
