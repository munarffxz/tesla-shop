# Generated by Django 5.0.7 on 2024-07-25 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SparePart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('articul', models.CharField(max_length=255, unique=True)),
                ('model', models.CharField(max_length=255)),
                ('marka', models.CharField(max_length=255)),
                ('year', models.PositiveIntegerField()),
                ('pokolenie', models.CharField(max_length=255)),
                ('primechanie', models.TextField(blank=True, null=True)),
                ('nomer_zapchasti', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]