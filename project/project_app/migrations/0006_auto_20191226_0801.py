# Generated by Django 2.2.6 on 2019-12-26 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0005_auto_20191225_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regiest_form',
            name='deptartment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deptartment', to='project_app.Department'),
        ),
    ]
