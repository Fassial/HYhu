# Generated by Django 2.1.3 on 2018-11-03 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signUp', '0005_auto_20181103_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='signup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='signup_set', to='signUp.SignUp'),
        ),
    ]
