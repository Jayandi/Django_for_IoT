# Generated by Django 3.1.2 on 2020-10-19 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20201019_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='topic_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.topics'),
        ),
    ]
