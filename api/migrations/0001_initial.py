# Generated by Django 5.1.6 on 2025-03-09 14:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=20)),
                ('status', models.BooleanField(default=False)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointmentDate', models.DateTimeField(auto_now_add=True)),
                ('imei', models.CharField(max_length=200)),
                ('device', models.CharField(choices=[('Phone', 'Phone'), ('Laptop', 'Laptop'), ('Desktop', 'Desktop')], max_length=200)),
                ('symptoms', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('status', models.BooleanField(default=False)),
                ('customerId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.customer', verbose_name='Customer name')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Technician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/TechProfilePic/')),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.IntegerField()),
                ('is_free', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DeviceDischargeDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('releaseDate', models.DateField()),
                ('daySpent', models.PositiveIntegerField()),
                ('storageCharge', models.PositiveIntegerField()),
                ('repairCost', models.PositiveIntegerField()),
                ('technicianFee', models.PositiveIntegerField()),
                ('OtherCharge', models.PositiveIntegerField()),
                ('total', models.PositiveIntegerField()),
                ('appointmentId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.appointment')),
                ('customerId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.customer', verbose_name='Customer name')),
                ('assignedTechnicianName', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.technician', verbose_name='Technician name')),
            ],
            options={
                'verbose_name_plural': 'Device Discharge Details',
                'ordering': ['-releaseDate'],
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='assignedTechnicianId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.technician', verbose_name='Technician name'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='assignedTechnicianId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.technician', verbose_name='Technician name'),
        ),
    ]
