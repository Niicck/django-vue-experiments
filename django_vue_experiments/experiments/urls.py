from typing import Type

from django.urls import URLResolver, path

from .views import ExperimentView, experiment_view_classes


def experiment_view_path(view_cls: Type[ExperimentView]) -> URLResolver:
    """
    Example:
        experiment_view_path(Experiment0View)

        Returns:
            path(
                "0",
                views.Experiment0View.as_view(),
                name="experiment_0",
            )
    """
    return path(
        str(view_cls.number),
        view_cls.as_view(),
        name=view_cls.path_name(),
    )


urlpatterns = [experiment_view_path(view_cls) for view_cls in experiment_view_classes]
