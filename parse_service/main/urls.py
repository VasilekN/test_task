from django.urls import path
from . import views

urlpatterns = [
    path("create", views.create_page),
    path("<int:object_id>", views.get_object),
    path("list", views.get_list)
]
