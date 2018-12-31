# Generated by Django 2.1.1 on 2018-12-31 04:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=140, unique=True)),
                ('service_type', models.CharField(choices=[('Manual', 'Manual'), ('Auto', 'Auto')], default='Auto', max_length=10)),
                ('duration', models.PositiveIntegerField(default=1)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('time', models.TimeField(default=django.utils.timezone.now)),
                ('instructor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='instructor', to='accounts.Profile')),
                ('name', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
            ],
        ),
    ]
