# Generated by Django 4.2.4 on 2023-09-17 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0002_rename_core_dell_laptop_spec_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='infinix_phone',
            old_name='space',
            new_name='storage',
        ),
        migrations.RenameField(
            model_name='redmi_phone',
            old_name='space',
            new_name='storage',
        ),
        migrations.RenameField(
            model_name='techno_phone',
            old_name='space',
            new_name='storage',
        ),
    ]