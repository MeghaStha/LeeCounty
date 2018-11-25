# Generated by Django 2.1.3 on 2018-11-25 00:30

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodDesert', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='leedata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=3160)),
            ],
        ),
        migrations.AlterModelOptions(
            name='fooddesert',
            options={'ordering': ('name',), 'verbose_name_plural': 'foodDesert'},
        ),
        migrations.AlterField(
            model_name='fooddesert',
            name='geometry',
            field=django.contrib.gis.db.models.fields.PointField(srid=3160),
        ),
    ]