import os
from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel, StreamFieldPanel
from wagtail.search import index

from streams import blocks


def file_path(instance, filename):
    basefilename, file_extension= os.path.splitext(filename)
    a_filename = 'ucc_'
    return f'files/{a_filename}{file_extension}'


class HomePage(Page):
    parent_page_types = ['wagtailcore.Page']
    subpage_types = []
    max_count = 1

    logo_text = models.CharField(_('Logotype long'), max_length=50, blank=True)
    logo_abreviation = models.CharField(_('logo abbreviation'), max_length=5, blank=True)
    logo_image = models.FileField(blank=True, upload_to="images/")
    text_intro = models.TextField(blank=True)
    text_intro_title = models.TextField(blank=True)
    youtube_video_id = models.CharField(_('Youtube video ID'), max_length=50, blank=True)

    text_prologue_title = models.TextField(blank=True)
    text_prologue = models.TextField(blank=True)

    partners_logo = StreamField([  # partners_logo_cards
        ("partners_logo_cards", blocks.PartnerLogo()),
    ],
            null=True,
            blank=True,
            use_json_field=True,
    )
    projects_block = StreamField([  # partners_logo_cards
        ("projects_block", blocks.Projects()),
    ],
            null=True,
            blank=True,
            use_json_field=True,
    )

    why_block = StreamField([
        ("text_why", blocks.TextWhy()),
    ],
            null=True,
            blank=True,
            use_json_field=True,
    )
    how_block = StreamField([
        ("text_how", blocks.TextHow()),
    ],
            null=True,
            blank=True,
            use_json_field=True,
    )
    who_block = StreamField([
        ("text_who", blocks.TextWho()),
    ],
            null=True,
            blank=True,
            use_json_field=True,
    )
    guiding = StreamField([
        ("text_guiding", blocks.TextGuiding()),
    ],
            null=True,
            blank=True,
            use_json_field=True,
    )
    text_list_next_title = models.TextField(blank=True)
    text_list_next = models.TextField(blank=True)
    media_about = StreamField([
        ("cards_media", blocks.CardMediaAbout()),
    ],
            null=True,
            blank=True,
            use_json_field=True,
    )
    footer_logo = StreamField([  # footer_logo_cards
        ("footer_logo_cards", blocks.FooterLogo()),
    ],
            null=True,
            blank=True,
            use_json_field=True,
    )
    text_partners = models.TextField(blank=True)
    text_copyright = models.TextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('logo_abreviation'),
        FieldPanel('logo_text'),
        FieldPanel('logo_image'),
        FieldPanel('text_intro', classname="full"),
        FieldPanel('youtube_video_id'),
        FieldPanel('text_prologue_title'),
        FieldPanel('text_prologue'),
        FieldPanel("partners_logo"),
        FieldPanel("projects_block"),
        FieldPanel("why_block"),
        FieldPanel("how_block"),
        FieldPanel("who_block"),
        FieldPanel("guiding"),
        FieldPanel('text_list_next_title'),
        FieldPanel('text_list_next'),
        FieldPanel("media_about"),
        FieldPanel("footer_logo"),
        FieldPanel('text_partners'),
        FieldPanel('text_copyright'),
    ]