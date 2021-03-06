# Generated by Django 2.2.10 on 2020-07-18 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0024_auto_20200718_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urlchecking',
            name='id',
        ),
        migrations.RemoveField(
            model_name='urlcheckingresult',
            name='id',
        ),
        migrations.AlterField(
            model_name='urlchecking',
            name='library',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pages.Library'),
        ),
        migrations.AlterField(
            model_name='urlcheckingresult',
            name='library',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pages.Library'),
        ),
    ]
