# -*- coding: utf-8 -*-
import json

from django.db import migrations

from appsembleredx import app_settings


def get_models(apps):
    CourseMode = apps.get_model("course_modes", "CourseMode")
    return (CourseMode,)


def change_audit_course_modes(apps, schema_editor):
    """ switch any audit course modes to our default mode slug
    """
    (CourseMode, ) = get_models(apps)

    for cm in CourseMode.objects.all():
        if cm.mode_slug == 'audit':
            cm.mode_slug = app_settings.DEFAULT_COURSE_MODE_SLUG
            cm.mode_display_name = app_settings.mode_name_from_slug
            cm.save()


class Migration(migrations.Migration):

    dependencies = [
        ('course_modes', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(change_audit_course_modes),
    ]