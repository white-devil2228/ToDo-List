from django.urls import path
from .views import *
from django.views.generic import RedirectView

urlpatterns = [
    path("", homeView, name="homeView"),
    path("complete/<id>",completeTaskView, name="completeTaskView"),
    path("edit/<id>",editTaskView, name="editTaskView"),
    path("delete/<id>",deleteTaskView, name="deleteTaskView"),
    path("delete/",deleteAllTaskView, name="deleteAllTaskView"),
    path('favicon.ico', RedirectView.as_view(url='/static/images/favicon.ico', permanent=True)),
]