# Generated by Django 5.0.1 on 2024-02-24 14:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_postulante_total_experiencia_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='postulante',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='perfil_postulante', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='perfil_admin', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Admin',
            },
        ),
    ]