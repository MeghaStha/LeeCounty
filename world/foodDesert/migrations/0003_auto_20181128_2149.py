# Generated by Django 2.1.3 on 2018-11-28 21:49

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodDesert', '0002_auto_20181125_0030'),
    ]

    operations = [
        migrations.CreateModel(
            name='foodlo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_na', models.CharField(max_length=254)),
                ('company_na', models.CharField(max_length=254)),
                ('primary_ad', models.CharField(max_length=254)),
                ('primary_ci', models.CharField(max_length=254)),
                ('census_tra', models.BigIntegerField()),
                ('census_blo', models.BigIntegerField()),
                ('x', models.FloatField()),
                ('latitude', models.BigIntegerField()),
                ('y_1', models.FloatField()),
                ('y', models.FloatField()),
                ('longitude', models.BigIntegerField()),
                ('naics_code', models.BigIntegerField()),
                ('naics_desc', models.CharField(max_length=254)),
                ('gender', models.CharField(max_length=254)),
                ('title_desc', models.CharField(max_length=254)),
                ('contact_et', models.CharField(max_length=254)),
                ('hq_branch_field', models.CharField(max_length=254)),
                ('year_first', models.BigIntegerField()),
                ('population', models.CharField(max_length=254)),
                ('source', models.CharField(max_length=254)),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='leepop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid', models.BigIntegerField()),
                ('statefp', models.CharField(max_length=2)),
                ('countyfp', models.CharField(max_length=3)),
                ('tractce', models.CharField(max_length=6)),
                ('blkgrpce', models.CharField(max_length=1)),
                ('geoid', models.CharField(max_length=12)),
                ('namelsad', models.CharField(max_length=13)),
                ('mtfcc', models.CharField(max_length=5)),
                ('funcstat', models.CharField(max_length=1)),
                ('aland', models.FloatField()),
                ('awater', models.FloatField()),
                ('intptlat', models.CharField(max_length=11)),
                ('intptlon', models.CharField(max_length=12)),
                ('id_1', models.CharField(max_length=50)),
                ('id2', models.FloatField()),
                ('geo_id', models.FloatField()),
                ('id_12', models.FloatField()),
                ('id3', models.FloatField()),
                ('geo_id2', models.FloatField()),
                ('geo_displa', models.CharField(max_length=254)),
                ('d001', models.BigIntegerField()),
                ('area', models.FloatField()),
                ('shape_leng', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('popden', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.DeleteModel(
            name='leedata',
        ),
    ]
