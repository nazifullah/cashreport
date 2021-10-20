# Generated by Django 3.2.7 on 2021-10-16 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fiscal_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Receivable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recieveable_amount', models.DecimalField(decimal_places=2, max_digits=18)),
                ('name', models.TextField(blank=True, null=True)),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='receivable', to='budget_book.year')),
            ],
        ),
        migrations.CreateModel(
            name='Openingbalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opening_amount', models.DecimalField(decimal_places=2, max_digits=18)),
                ('account_name', models.CharField(max_length=200)),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='openingbalance', to='budget_book.year')),
            ],
        ),
        migrations.CreateModel(
            name='Commitment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(db_column='Amount', decimal_places=2, max_digits=18)),
                ('donorname', models.TextField(blank=True, db_column='DonorName', null=True)),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='commitment', to='budget_book.year')),
            ],
        ),
    ]