# Generated by Django 4.0.5 on 2022-06-10 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_alter_mission_options_alter_planet_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Planet',
            new_name='SpaceObject',
        ),
        migrations.AlterModelOptions(
            name='spaceobject',
            options={'verbose_name': 'Небесное тело', 'verbose_name_plural': 'Небесные тела'},
        ),
        migrations.RenameField(
            model_name='mission',
            old_name='planet',
            new_name='space_object',
        ),
        migrations.DeleteModel(
            name='Satellites',
        ),
    ]