# Generated by Django 4.2.5 on 2023-09-28 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0006_alter_project_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='portfolio',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.portfolio'),
        ),
    ]