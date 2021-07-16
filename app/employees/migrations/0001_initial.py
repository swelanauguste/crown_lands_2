# Generated by Django 3.2.5 on 2021-07-16 08:58

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
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employment_id', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('tel', models.CharField(blank=True, max_length=25, null=True)),
                ('position', models.CharField(blank=True, choices=[('CLERK', 'CLERK'), ('SECRETARY', 'SECRETARY'), ('CROWN LANDS TECHNICIAN', 'CROWN LANDS TECHNICIAN'), ('CROWN LANDS ASSISTANT', 'CROWN LANDS ASSISTANT'), ('CROWN LANDS OFFICER', 'CROWN LANDS OFFICER'), ('SURVEYER', 'SURVEYER'), ('DEPUTY COMMISSIONER OF CROWN LANDS', 'DEPUTY COMMISSIONER OF CROWN LANDS'), ('COMMISSIONER OF CROWN LANDS', 'COMMISSIONER OF CROWN LANDS')], max_length=200, null=True)),
                ('grade', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=200, null=True)),
                ('is_commissioner', models.BooleanField(default=False)),
                ('is_deputy_commissioner', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254)),
                ('employee', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
