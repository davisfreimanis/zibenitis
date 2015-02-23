# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('mid_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_added', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
