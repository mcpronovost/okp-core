from django.conf import settings
from django.views.generic import TemplateView


class OkpTemplateView(TemplateView):
    """Base template view that ensures CSRF cookie is set"""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        return response
