# Generated by Django 4.0.5 on 2022-06-10 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='spaceobject',
            name='type',
            field=models.CharField(choices=[('planet', 'Планета'), ('satellite', 'Спутник')], default=1, max_length=20, verbose_name='Тип'),
            preserve_default=False,
        ),
    ]
