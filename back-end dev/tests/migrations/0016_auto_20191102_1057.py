# Generated by Django 2.2.5 on 2019-11-02 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0015_auto_20191102_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pass_dyntest',
            name='q_num',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]