# Generated by Django 2.0.7 on 2018-07-30 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('gps_x', models.DecimalField(decimal_places=7, default=0.0, max_digits=10)),
                ('gps_y', models.DecimalField(decimal_places=7, default=0.0, max_digits=10)),
                ('open_hours', models.CharField(max_length=100)),
                ('avg_visit_time', models.DurationField()),
                ('prices', models.CharField(max_length=100)),
                ('age_rules', models.CharField(max_length=20)),
                ('about', models.CharField(default='nothing here', max_length=1000)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('img', models.ImageField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('attractions', models.ManyToManyField(related_name='attractions', to='guidebase.Place')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='place',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guidebase.TypeOfPlace'),
        ),
    ]