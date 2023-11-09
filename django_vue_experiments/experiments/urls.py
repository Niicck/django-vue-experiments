from django.urls import path

from . import views

urlpatterns = [
    path(
        "0",
        views.Experiment0View.as_view(),
        name="exp0",
    ),
    path(
        "1",
        views.Experiment1View.as_view(),
        name="exp1",
    ),
]
