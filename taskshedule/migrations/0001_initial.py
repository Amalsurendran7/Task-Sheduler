# Generated by Django 4.1.7 on 2023-03-24 09:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AuthUser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('task', models.TextField()),
                ('task_date', models.DateTimeField(auto_now_add=True)),
                ('task_completed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task', to='AuthUser.customuser')),
            ],
        ),
    ]