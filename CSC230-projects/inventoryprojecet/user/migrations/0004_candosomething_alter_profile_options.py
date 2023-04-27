# Generated by Django 4.1.7 on 2023-04-27 16:29

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('user', '0003_remove_profile_address_remove_profile_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='CanDoSomething',
            fields=[
                ('permission_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.permission')),
            ],
            bases=('auth.permission',),
            managers=[
                ('objects', django.contrib.auth.models.PermissionManager()),
            ],
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': [('can_do_something', 'Can do something')]},
        ),
    ]