# Generated by Django 4.1.7 on 2023-03-28 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examsolution', '0002_boardsubtopic_examboard_paper_session_subject_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchStuff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_text', models.CharField(max_length=2000)),
            ],
        ),
    ]
