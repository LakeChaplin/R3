# Generated by Django 4.2.1 on 2023-11-26 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicians', '0003_alter_musicians_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='musicians',
            options={'ordering': ['-time_create']},
        ),
        migrations.AlterField(
            model_name='musicians',
            name='is_published',
            field=models.BooleanField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
        migrations.AddIndex(
            model_name='musicians',
            index=models.Index(fields=['-time_create'], name='musicians_m_time_cr_66f217_idx'),
        ),
    ]
