# Generated by Django 4.2.9 on 2024-02-08 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_specification'),
    ]

    operations = [
        migrations.AddField(
            model_name='specification',
            name='mobile_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.mobile'),
            preserve_default=False,
        ),
    ]
