# Generated by Django 5.0.3 on 2024-03-31 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0017_summons_delete_summonsform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drugs',
            name='drug_type',
            field=models.CharField(choices=[('Tablet', 'Tablet'), ('Capsule', 'Capsule'), ('Liquid', 'Liquid'), ('Injection', 'Injection'), ('Cream', 'Cream'), ('Spray', 'Spray')], max_length=20),
        ),
    ]
