# Generated by Django 2.2 on 2019-05-29 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0024_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('project_files', models.FileField(blank=True, null=True, upload_to='')),
                ('assigned_to', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.AlterField(
            model_name='employee',
            name='leaves',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(max_length=255),
        ),
    ]
