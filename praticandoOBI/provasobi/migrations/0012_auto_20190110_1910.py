# Generated by Django 2.1.4 on 2019-01-10 19:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provasobi', '0011_auto_20190110_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problema',
            name='numeroproblema',
            field=models.PositiveIntegerField(db_column='numeroProblema', default=1, validators=[django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='questao',
            name='numeroquestao',
            field=models.PositiveIntegerField(db_column='numeroQuestao', default=1, validators=[django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
    ]