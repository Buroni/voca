# Generated by Django 3.0.2 on 2020-03-15 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentences', '0003_sentence_reports'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentence',
            name='partition',
            field=models.IntegerField(default=0),
        ),
    ]
