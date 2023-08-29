# Generated by Django 4.2.4 on 2023-08-27 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='description',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='rating',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Bio', 'Biography'), ('type', 'type')], default='', max_length=128),
            preserve_default=False,
        ),
    ]
