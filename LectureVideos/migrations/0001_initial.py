# Generated by Django 4.2.1 on 2023-05-29 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('SubjectDetail', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='lecturevideos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('video_url', models.URLField(blank=True, null=True)),
                ('description', models.TextField()),
                ('video_file', models.FileField(blank=True, null=True, upload_to='uploads/videos/')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='uploads/thumbnails/')),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
                ('duration_mint', models.IntegerField(blank=True, null=True)),
                ('subjects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SubjectDetail.subjects')),
            ],
        ),
    ]
