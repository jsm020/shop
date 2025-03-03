# Generated by Django 5.0.6 on 2024-06-05 07:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Soatlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=255)),
                ('tavsif', models.TextField()),
                ('narxi', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'Soatlar',
                'verbose_name_plural': 'Soatlar',
            },
        ),
        migrations.CreateModel(
            name='Soatlar_rasmlari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasmi', models.ImageField(upload_to='Soatlar/')),
                ('nomi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Soatlar', to='wristwatch.soatlar')),
            ],
            options={
                'verbose_name': 'Soatlar rasmlari',
                'verbose_name_plural': 'Soatlar rasmlari',
            },
        ),
    ]
