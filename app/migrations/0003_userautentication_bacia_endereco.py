# Generated by Django 4.1.7 on 2023-06-16 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_endereco_numero'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAutentication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('password', models.CharField(max_length=128)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='bacia',
            name='endereco',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.endereco'),
            preserve_default=False,
        ),
    ]
