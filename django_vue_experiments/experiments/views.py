from typing import Type

from django.core.exceptions import ImproperlyConfigured
from django.views.generic import TemplateView


class ExperimentView(TemplateView):
    number: int
    description: str

    def get_template_names(self):
        if not self.template_name:
            raise ImproperlyConfigured(
                "You must provide a template_name for your ExperimentView."
            )
        return [f"experiments/{self.template_name}"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["number"] = self.number
        context["description"] = self.description
        context["embed"] = self.request.GET.get("embed", "false") == "true"
        return context

    @classmethod
    def path_name(cls) -> str:
        return f"experiment_{cls.number}"


class Experiment0(ExperimentView):
    number = 0
    description = "Load JavaScript with a script tag"
    template_name = "000_script_tag.html"


class Experiment1(ExperimentView):
    number = 1
    description = "Inject a Vue Single File Component into a Django template"
    template_name = "001_vue_mvp.html"


experiment_view_classes: list[Type[ExperimentView]] = [
    Experiment0,
    Experiment1,
]
