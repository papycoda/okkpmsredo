# Generated by Django 3.1 on 2020-10-31 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('employees', '0027_auto_20201031_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='branch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='company.branch'),
        ),
    ]
