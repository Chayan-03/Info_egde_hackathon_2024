# Generated by Django 5.0.7 on 2024-07-17 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_remove_report_receiver_remove_report_transaction_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcardmodel',
            name='is_locked',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='debitcardmodel',
            name='is_locked',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='netbankingdetailsmodel',
            name='is_locked',
            field=models.BooleanField(),
        ),
    ]
