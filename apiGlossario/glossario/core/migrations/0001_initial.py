# Generated by Django 2.1.7 on 2020-04-30 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Termo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('termo', models.CharField(max_length=150)),
                ('area', models.CharField(max_length=75)),
                ('expressao', models.CharField(max_length=150)),
                ('definicao', models.TextField()),
                ('urlImg', models.CharField(max_length=255)),
            ],
        ),
    ]
