from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.templatetags import wagtailcore_tags
from wagtail.fields import RichTextField
from wagtail.models import Page


class HomePage(Page):
    content = RichTextField(blank=True)

    def content_html(self):
        return wagtailcore_tags.richtext(self.content)

    content_panels = Page.content_panels + [
        FieldPanel("content"),
    ]

    api_fields = [
        APIField("content_html"),
    ]
