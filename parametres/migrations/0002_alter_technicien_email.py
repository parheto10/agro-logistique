# Generated by Django 3.2.6 on 2021-11-19 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametres', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technicien',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
