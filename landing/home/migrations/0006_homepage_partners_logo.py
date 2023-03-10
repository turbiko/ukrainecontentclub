# Generated by Django 4.1.7 on 2023-02-17 19:01

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_homepage_who_block'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='partners_logo',
            field=wagtail.fields.StreamField([('partners_logo_cards', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Add your title', required=True)), ('width', wagtail.blocks.IntegerBlock(help_text='Width in vw for all logos added', required=True)), ('footer_logo_cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('logo_title', wagtail.blocks.CharBlock(max_length=200, required=False)), ('logo_url', wagtail.blocks.URLBlock(default='', help_text='logo owner site link', required=False))])))]))], blank=True, null=True, use_json_field=None),
        ),
    ]
