# Generated by Django 2.2.6 on 2019-12-26 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0007_auto_20191226_0806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regiest_form',
            name='department',
        ),
        migrations.AddField(
            model_name='regiest_form',
            name='deptartment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='project_app.Department'),
        ),
    ]
