# Generated by Django 2.1.1 on 2019-01-01 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_learneraddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructorqualification',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]