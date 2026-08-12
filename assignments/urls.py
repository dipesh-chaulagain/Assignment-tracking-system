from.views import AssignmentViewSet
from django.urls import path

urlpatterns = [
    # GET /api/assignments/          -> list all
    # POST /api/assignments/          -> create one
    path("", AssignmentViewSet.as_view({"get": "list", "post": "create"})),
]