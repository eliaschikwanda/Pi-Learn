# Generated by Django 4.1.7 on 2022-01-01 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examsolution', '0019_fullquestionanswer_a_raw_mark_req_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fullquestionanswer',
            name='general_exam_report_cmnt',
            field=models.CharField(blank=True, max_length=20000, null=True),
        ),
    ]
