# Generated by Django 4.2.1 on 2023-05-29 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ClassName', '0004_alter_classname_class_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('instructure_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('subject_image', models.ImageField(blank=True, null=True, upload_to='uploads/subject_images/')),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='ClassName.classname')),
            ],
        ),
    ]
