# Generated by Django 4.2.1 on 2023-05-29 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClassName', '0002_alter_classname_class_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classname',
            name='class_image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/subject_images/'),
        ),
    ]
