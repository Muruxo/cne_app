# Generated by Django 5.0.2 on 2024-02-27 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_user_postulante_usuario_postulante_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educacion',
            name='nivel_edu',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
