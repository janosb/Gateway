# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chi2Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(max_length=200, blank=True)),
                ('chi2dof', models.FloatField(null=True, blank=True)),
                ('chi2dof_bin', models.FloatField(null=True, blank=True)),
                ('dof', models.IntegerField(null=True, blank=True)),
                ('dofb', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'chi2test',
            },
        ),
        migrations.CreateModel(
            name='Fluxvals',
            fields=[
                ('spec_id', models.IntegerField(serialize=False, primary_key=True)),
                ('wavelength', models.FloatField()),
                ('luminosity', models.FloatField(null=True, blank=True)),
                ('photon_count', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'fluxvals',
            },
        ),
        migrations.CreateModel(
            name='LCVals',
            fields=[
                ('lc_id', models.IntegerField(serialize=False, primary_key=True)),
                ('t_expl', models.IntegerField()),
                ('b_landolt', models.FloatField(null=True, blank=True)),
                ('r_landolt', models.FloatField(null=True, blank=True)),
                ('i_landolt', models.FloatField(null=True, blank=True)),
                ('ux_landolt', models.FloatField(null=True, blank=True)),
                ('v_landolt', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'lcvals',
            },
        ),
        migrations.CreateModel(
            name='LightCurves',
            fields=[
                ('model_id', models.IntegerField()),
                ('lc_id', models.IntegerField(serialize=False, primary_key=True)),
                ('theta', models.FloatField(null=True, blank=True)),
                ('phi', models.FloatField(null=True, blank=True)),
                ('b_lan_max', models.FloatField(null=True, blank=True)),
                ('r_lan_max', models.FloatField(null=True, blank=True)),
                ('i_lan_max', models.FloatField(null=True, blank=True)),
                ('ux_lan_max', models.FloatField(null=True, blank=True)),
                ('v_lan_max', models.FloatField(null=True, blank=True)),
                ('t_b_lan_max', models.FloatField(null=True, blank=True)),
                ('t_r_lan_max', models.FloatField(null=True, blank=True)),
                ('t_i_lan_max', models.FloatField(null=True, blank=True)),
                ('t_ux_lan_max', models.FloatField(null=True, blank=True)),
                ('t_v_lan_max', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'lightcurves',
            },
        ),
        migrations.CreateModel(
            name='MetaDd2D',
            fields=[
                ('model_id', models.IntegerField(serialize=False, primary_key=True)),
                ('pub_id', models.IntegerField()),
                ('modelname', models.CharField(max_length=40, blank=True)),
                ('mass_wd', models.FloatField(null=True, blank=True)),
                ('percent_carbon', models.FloatField(null=True, blank=True)),
                ('percent_oxygen', models.FloatField(null=True, blank=True)),
                ('n_ignit', models.IntegerField(null=True, blank=True)),
                ('r_min_ignit', models.FloatField(null=True, blank=True)),
                ('cos_alpha', models.FloatField(null=True, blank=True)),
                ('stdev', models.FloatField(null=True, blank=True)),
                ('ka_min', models.FloatField(null=True, blank=True)),
                ('rho_min', models.FloatField(null=True, blank=True)),
                ('rho_max', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'meta_dd2d',
            },
        ),
        migrations.CreateModel(
            name='MetaNsm1D',
            fields=[
                ('pub_id', models.IntegerField()),
                ('model_id', models.IntegerField(serialize=False, primary_key=True)),
                ('modelname', models.CharField(max_length=40, blank=True)),
                ('m_ej', models.FloatField(null=True, blank=True)),
                ('beta', models.FloatField(null=True, blank=True)),
                ('n', models.FloatField(null=True, blank=True)),
                ('delta', models.FloatField(null=True, blank=True)),
                ('composition', models.CharField(max_length=4)),
            ],
            options={
                'db_table': 'meta_nsm1d',
            },
        ),
        migrations.CreateModel(
            name='MetaPi1D',
            fields=[
                ('pub_id', models.IntegerField()),
                ('model_id', models.IntegerField(serialize=False, primary_key=True)),
                ('modelname', models.CharField(max_length=15, blank=True)),
                ('t_expl', models.FloatField(null=True, blank=True)),
                ('mass', models.FloatField(null=True, blank=True)),
                ('star_type', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'meta_pi1d',
            },
        ),
        migrations.CreateModel(
            name='Publications',
            fields=[
                ('modeltype', models.CharField(max_length=40, verbose_name='Model Type', blank=True)),
                ('modeldim', models.IntegerField(verbose_name='Model Dimension')),
                ('date_entered', models.DateField(verbose_name='Date Entered')),
                ('citation', models.CharField(max_length=200, verbose_name='Citation', blank=True)),
                ('type', models.CharField(max_length=10, verbose_name='Type', blank=True)),
                ('pub_id', models.IntegerField(serialize=False, verbose_name='Publication ID', primary_key=True)),
                ('fullname', models.CharField(max_length=200, blank=True)),
                ('shortname', models.CharField(max_length=200, blank=True)),
                ('is_public', models.BooleanField()),
                ('metatype', models.CharField(max_length=20, blank=True)),
                ('summary', models.TextField()),
                ('url', models.CharField(max_length=200, blank=True)),
            ],
            options={
                'db_table': 'publications',
            },
        ),
        migrations.CreateModel(
            name='Spectra',
            fields=[
                ('model_id', models.IntegerField()),
                ('spec_id', models.IntegerField(serialize=False, primary_key=True)),
                ('t_expl', models.FloatField(null=True, blank=True)),
                ('mu', models.FloatField(null=True, blank=True)),
                ('phi', models.FloatField(null=True, blank=True)),
                ('metatype', models.CharField(max_length=20, blank=True)),
            ],
            options={
                'db_table': 'spectra',
            },
        ),
    ]
