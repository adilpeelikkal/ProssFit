# Generated by Django 3.0.2 on 2020-01-10 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=501)),
                ('last_name', models.CharField(max_length=501)),
                ('email', models.EmailField(max_length=501)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
