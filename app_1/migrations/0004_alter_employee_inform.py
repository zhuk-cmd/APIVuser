# Generated by Django 3.2.6 on 2021-08-17 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0003_alter_employee_inform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='inform',
            field=models.DecimalField(decimal_places=4, max_digits=12, verbose_name='Информация о выплаченной зп'),
        ),
    ]