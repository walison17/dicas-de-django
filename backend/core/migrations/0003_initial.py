# Generated by Django 4.1.3 on 2022-12-24 09:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='data de nascimento')),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('rg', models.CharField(blank=True, max_length=10, null=True)),
                ('cpf', models.CharField(blank=True, max_length=11, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT,
                 to=settings.AUTH_USER_MODEL, verbose_name='usuário')),
            ],
            options={
                'verbose_name': 'perfil',
                'verbose_name_plural': 'perfis',
                'ordering': ('user__first_name',),
            },
        ),
    ]
