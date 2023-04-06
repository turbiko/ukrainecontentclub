# Generated by Django 4.1.7 on 2023-04-05 21:55

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_homepage_projects_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='projects_block',
            field=wagtail.fields.StreamField([('projects_block', wagtail.blocks.StructBlock([('title_projects', wagtail.blocks.CharBlock(help_text='Add your title', required=True)), ('text_card', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('text', wagtail.blocks.CharBlock(max_length=300, required=False)), ('learn_more_url', wagtail.blocks.URLBlock(help_text='Link URL.', required=False))])))]))], blank=True, null=True, use_json_field=None),
        ),
    ]