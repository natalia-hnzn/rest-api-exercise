# Generated by Django 4.2.2 on 2023-06-21 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='avaliacao',
            unique_together={('professor', 'aluno')},
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='nota',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
