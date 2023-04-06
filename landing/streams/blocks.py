from wagtail import blocks
from wagtail.templatetags.wagtailcore_tags import richtext
from wagtail.images.blocks import ImageChooserBlock

class PartnerLogo(blocks.StructBlock):
    """ logotypes: image, vw size, calculated aspect ratio"""

    title = blocks.CharBlock(required=True, help_text="Add your title")
    width = blocks.IntegerBlock(required=True, help_text="Width in % in block for all logos added")

    partners_logo_cards = blocks.ListBlock(
            blocks.StructBlock(
                    [
                        ("image", ImageChooserBlock(required=True)),
                        ("logo_title", blocks.CharBlock(required=False, max_length=200)),
                        (
                            "logo_url",
                            blocks.URLBlock(
                                    required=False,
                                    default="",
                                    help_text="logo owner site link",  # noqa
                            ),
                        ),

                    ]))

    class Meta:  # __PP_noqa
        template = "streams/partners_logos.html"
        icon = "placeholder"
        label = "Partners Logo with size"

class Projects(blocks.StructBlock):
    """Text Cards with text and title"""

    title_projects = blocks.CharBlock(required=True, help_text="Add your title")


    text_card = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("text", blocks.CharBlock(required=False, max_length=300)),
                ("description", blocks.CharBlock(required=False, max_length=300)),
                (
                    "learn_more_url",
                    blocks.URLBlock(
                            required=False,
                            help_text="Link URL.",  # noqa
                    ),
                ),
        ]))

    class Meta:  # noqa
        template = "streams/block_projects.html"
        icon = "placeholder"
        label = "Projects block"

class TextWhy(blocks.StructBlock):
    """Text Cards with title and texts  """

    title_why = blocks.TextBlock(required=True, help_text="Add your why title")

    text_cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("text", blocks.CharBlock(required=False, max_length=300)),
        ]))

    class Meta:  # noqa
        template = "streams/block_why.html"
        icon = "placeholder"
        label = "Text Cards with text and title"

class TextHow(blocks.StructBlock):
    """Text Cards with title and texts  """

    title_how = blocks.TextBlock(required=True, help_text="Add your why title")

    text_cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("text", blocks.CharBlock(required=False, max_length=300)),
        ]))

    class Meta:  # noqa
        template = "streams/block_how.html"
        icon = "placeholder"
        label = "Text Cards with text and title"


class CardMediaAbout(blocks.StructBlock):
    """Cards with image and title and link."""

    title = blocks.CharBlock(required=True, help_text="Add your title")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=60)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),

            ]
        )
    )

    class Meta:  # noqa
        template = "streams/card_media.html"
        icon = "placeholder"
        label = "Staff Cards"


class TextWho(blocks.StructBlock):
    """Text Cards with text and title"""

    title_who = blocks.TextBlock(required=True, help_text="Add your title")

    text_cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("text", blocks.CharBlock(required=False, max_length=300)),
        ]))

    class Meta:  # noqa
        template = "streams/block_who.html"
        icon = "placeholder"
        label = "Text Cards with num and title"



class TextGuiding(blocks.StructBlock):
    """Text Cards with num, title and description"""

    title1 = blocks.TextBlock(required=True, help_text="Add your title")

    text_cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("number", blocks.IntegerBlock(required=False)),
                ("title", blocks.CharBlock(required=False, max_length=60)),
                ("description", blocks.CharBlock(required=False, max_length=200)),
        ]))

    class Meta:  # noqa
        template = "streams/text_guiding.html"
        icon = "placeholder"
        label = "Text Cards with num and title"


class FooterLogo(blocks.StructBlock):
    """ logotypes: image, real size, calculated aspect ratio"""

    title = blocks.CharBlock(required=True, help_text="Add your title")
    width = blocks.IntegerBlock(required=True, help_text="Width in vw for all logos added")

    footer_logo_cards = blocks.ListBlock(
            blocks.StructBlock(
                    [
                        ("image", ImageChooserBlock(required=True)),
                        ("logo_title", blocks.CharBlock(required=False, max_length=200)),
                        (
                            "logo_url",
                            blocks.URLBlock(
                                    required=False,
                                    default="",
                                    help_text="logo owner site link",  # noqa
                            ),
                        ),

                    ]))

    class Meta:  # __PP_noqa
        template = "streams/footer_logo_block.html"
        icon = "placeholder"
        label = "Footer Logo with size"