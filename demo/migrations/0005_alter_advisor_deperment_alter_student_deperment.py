# Generated by Django 4.2.5 on 2023-10-02 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_rename_name_advisor_aname_remove_course_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advisor',
            name='deperment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advisor', to='demo.depertment'),
        ),
        migrations.AlterField(
            model_name='student',
            name='deperment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student', to='demo.depertment'),
        ),
    ]