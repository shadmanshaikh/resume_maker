# Generated by Django 4.1.7 on 2023-04-06 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_technology_flag_alter_technology_coding_skill_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Technology',
        ),
    ]