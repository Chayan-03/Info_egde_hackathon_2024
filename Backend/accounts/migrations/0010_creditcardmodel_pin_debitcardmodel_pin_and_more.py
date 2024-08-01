# Generated by Django 5.0.7 on 2024-07-15 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_virtualcreditcardmodel_virtualdebitcardmodel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditcardmodel',
            name='pin',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='debitcardmodel',
            name='pin',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='virtualcreditcardmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='virtualcreditcardmodel',
            name='pin',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='virtualdebitcardmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='virtualdebitcardmodel',
            name='pin',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='virtualnetbankingdetailsmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
