# Generated by Django 5.0.1 on 2024-02-23 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_experiencia_id_experiencia_fk_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experiencia',
            old_name='area_exo',
            new_name='area',
        ),
        migrations.RenameField(
            model_name='experiencia',
            old_name='cargo_exp',
            new_name='cargo',
        ),
        migrations.RenameField(
            model_name='experiencia',
            old_name='descripcion_exp',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='experiencia',
            old_name='empresa_exp',
            new_name='empresa',
        ),
        migrations.RenameField(
            model_name='experiencia',
            old_name='ffinal_exp',
            new_name='fecha_final',
        ),
        migrations.RenameField(
            model_name='experiencia',
            old_name='finicio_exp',
            new_name='fecha_inicio',
        ),
        migrations.RenameField(
            model_name='experiencia',
            old_name='pais_exp',
            new_name='pais',
        ),
    ]
