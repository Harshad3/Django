# Generated by Django 3.2.4 on 2021-06-20 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featuredpls',
            name='img',
            field=models.ImageField(default='Pictures', upload_to='Pictures'),
        ),
    ]