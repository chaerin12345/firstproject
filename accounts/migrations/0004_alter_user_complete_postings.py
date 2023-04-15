# Generated by Django 3.2.18 on 2023-04-13 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
        ('accounts', '0003_user_complete_postings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='complete_postings',
            field=models.ManyToManyField(related_name='com_users', to='app.Today'),
        ),
    ]