# Generated by Django 4.2.3 on 2023-08-05 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desktop',
            fields=[
                ('voucher_numberd', models.CharField(blank=True, db_column='Voucher_Number', default=None, max_length=50, primary_key=True, serialize=False)),
                ('monitor_brand_name', models.CharField(blank=True, db_column='Monitor_Brand_Name', max_length=50, null=True)),
                ('monitor_model_name', models.CharField(blank=True, db_column='Monitor_Model_Name', max_length=50, null=True)),
                ('cpu_brand_name', models.CharField(blank=True, db_column='CPU_Brand_Name', max_length=50, null=True)),
                ('cpu_model_name', models.CharField(blank=True, db_column='CPU_Model_Name', max_length=50, null=True)),
                ('cpu_processor', models.CharField(blank=True, db_column='CPU_Processor', max_length=50, null=True)),
                ('cpu_ram', models.CharField(blank=True, db_column='CPU_RAM', max_length=50, null=True)),
                ('keyboard_serial_number', models.CharField(blank=True, db_column='KEYBOARD_Serial_Number', max_length=50, null=True)),
                ('mouse_serial_number', models.CharField(blank=True, db_column='MOUSE_Serial_Number', max_length=50, null=True)),
                ('grant', models.CharField(blank=True, db_column='Grant', max_length=50, null=True)),
                ('year_of_purchase', models.CharField(blank=True, db_column='Year_Of_PurchaseD', max_length=4, null=True)),
                ('group', models.CharField(blank=True, db_column='Group_D', max_length=50, null=True)),
                ('nomenclature', models.CharField(blank=True, db_column='Nomenclature_D', max_length=250, null=True)),
            ],
            options={
                'db_table': 'desktop',
                'managed': False,
            },
        ),
    ]
