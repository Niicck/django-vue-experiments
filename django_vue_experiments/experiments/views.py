from django.core.exceptions import ImproperlyConfigured
from django.views.generic import TemplateView


class ExperimentView(TemplateView):
    def get_template_names(self):
        if not self.template_name:
            raise ImproperlyConfigured(
                "You must provide a template_name for your ExperimentView."
            )
        return [f"experiments/{self.template_name}"]


class Experiment0View(ExperimentView):
    template_name = "000_script_tag.html"


class Experiment1View(ExperimentView):
    template_name = "001_vue_mvp.html"
