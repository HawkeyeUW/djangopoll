# Generated by Django 2.1.11 on 2021-03-10 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0002_category_squashed_0003_auto_20210310_0133'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]