# Generated by Django 4.1.1 on 2022-09-29 01:29

from django.db import migrations

def populate_status(apps, schemaeditor):
    entries = {
        "published": "A post that appears on the site (to all users).",
        "draft": "A post being updated.",
        "archived": "A post no longer on the site."
    }
    Status = apps.get_model("posts", "Status")
    for name, desc in entries.items():
        status_obj = Status(name=name, description=desc)
        status_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_status_alter_post_subtitle_alter_post_title'),
    ]

    operations = [migrations.RunPython(populate_status)]
