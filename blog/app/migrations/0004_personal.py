# Generated by Django 5.0.2 on 2024-02-29 22:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_educacion_id_educacion_fk_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=144)),
                ('apellido', models.CharField(max_length=144)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='perfil_admin', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Personal',
            },
        ),
    ]