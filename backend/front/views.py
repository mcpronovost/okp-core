from django.http import HttpResponse
from django.template.loader import render_to_string


def app(request):
    template = render_to_string("index.html", {})
    template = template.replace("/_astro/", "/static/_astro/")
    return HttpResponse(template)
