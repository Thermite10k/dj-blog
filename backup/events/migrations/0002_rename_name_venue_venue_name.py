# Generated by Django 3.2.5 on 2021-08-02 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venue',
            old_name='name',
            new_name='Venue_name',
        ),
    ]