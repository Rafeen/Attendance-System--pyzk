# Generated by Django 2.2.1 on 2019-07-31 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device_user',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='Unknown', max_length=30)),
                ('password', models.CharField(blank=True, max_length=255)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('user_id',),
            },
        ),
    ]
