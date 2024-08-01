# Generated by Django 5.0.7 on 2024-07-13 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpamDetectionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('spam_not_spam', models.BooleanField()),
                ('risk_associated', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TransactionPatternDetectionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_location', models.CharField(max_length=255)),
                ('sender_device_id', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sender_upi_ac_no', models.CharField(max_length=255)),
                ('receiver_upi_ac_no', models.CharField(max_length=255)),
                ('sender_acc_balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mode_of_transaction', models.CharField(max_length=255)),
                ('frequency_of_transaction', models.IntegerField()),
                ('fraud_not_fraud', models.BooleanField()),
            ],
        ),
    ]
