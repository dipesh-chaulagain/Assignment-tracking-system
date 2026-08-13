from django.urls import path

from . import views

# Namespace for this URL file. It lets templates say
# {% url "assignments:assignment_list" %} instead of
# hard-coding "/" inside every template.
app_name = "assignments"

urlpatterns = [
    # An empty path ("") means "the root of this URL include".
    # The view `assignment_list` handles both GET and POST.
    path("", views.assignment_list, name="assignment_list"),
]
