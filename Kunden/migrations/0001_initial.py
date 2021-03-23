# Generated by Django 3.1.7 on 2021-02-24 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kunden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('Strasse', models.CharField(max_length=50)),
                ('Hausnummer', models.IntegerField()),
                ('Postleitzahl', models.IntegerField()),
                ('Stadt', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, verbose_name='Email Addresse')),
            ],
            options={
                'verbose_name': 'Kunde',
                'verbose_name_plural': 'Kunden',
            },
        ),
    ]
