# Generated by Django 4.1.4 on 2023-06-09 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("new_App", "0002_common"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Common",
            new_name="All_Users",
        ),
        migrations.AlterModelTable(
            name="all_users",
            table="All_Users",
        ),
    ]