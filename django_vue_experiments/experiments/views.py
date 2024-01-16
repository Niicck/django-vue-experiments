from typing import Type

from django.contrib import messages
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import redirect
from django.views.generic import TemplateView


class ExperimentView(TemplateView):
    number: int | str
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
    description = "Load JavaScript the old school way"
    template_name = "000_vanilla_js.html"


class Experiment1(ExperimentView):
    number = 1
    description = "Inject a Vue Single File Component into a Django template"
    template_name = "001_vue_mvp.html"


class SuccessMessageExperimentView(ExperimentView):
    def post(self, request, *args, **kwargs):
        messages.success(self.request, "Great Job! You pressed a button.")
        return redirect(self.path_name())


class Experiment2a(SuccessMessageExperimentView):
    number = "2a"
    description = "Default Django Messages"
    template_name = "002a_default_messages.html"


class Experiment2b(SuccessMessageExperimentView):
    number = "2b"
    description = "Vuetify Django Messages"
    template_name = "002b_vuetify_messages.html"


class React(ExperimentView):
    number = "react"
    description = "React"
    template_name = "react.html"


class Hello(ExperimentView):
    number = "hello"
    description = "Hello!"
    template_name = "hello.html"


# Add your view to this list to automatically create homepage links and url paths.
experiment_view_classes: list[Type[ExperimentView]] = [
    Experiment0,
    Experiment1,
    Experiment2a,
    Experiment2b,
    React,
    Hello,
]
