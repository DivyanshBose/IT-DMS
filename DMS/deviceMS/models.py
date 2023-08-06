from django.db import models
from django.contrib.auth.models import User



class Desktop(models.Model):
    voucher_numberd = models.CharField(db_column='Voucher_Number', max_length=50, blank=True, default=None, primary_key=True)
    monitor_brand_name = models.CharField(db_column='Monitor_Brand_Name', max_length=50, blank=True, null=True)
    monitor_model_name = models.CharField(db_column='Monitor_Model_Name', max_length=50, blank=True, null=True)
    cpu_brand_name = models.CharField(db_column='CPU_Brand_Name', max_length=50, blank=True, null=True)
    cpu_model_name = models.CharField(db_column='CPU_Model_Name', max_length=50, blank=True, null=True)
    cpu_processor = models.CharField(db_column='CPU_Processor', max_length=50, blank=True, null=True)
    cpu_ram = models.CharField(db_column='CPU_RAM', max_length=50, blank=True, null=True)
    keyboard_serial_number = models.CharField(db_column='KEYBOARD_Serial_Number', max_length=50, blank=True, null=True)
    mouse_serial_number = models.CharField(db_column='MOUSE_Serial_Number', max_length=50, blank=True, null=True)
    grant = models.CharField(db_column='Grant', max_length=50, blank=True, null=True)
    year_of_purchase = models.CharField(db_column='Year_Of_PurchaseD', blank=True, null=True ,max_length=4)
    group = models.CharField(db_column='Group_D', max_length=50, blank=True, null=True)
    nomenclature = models.CharField(db_column='Nomenclature_D', max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'desktop'
    
    def __str__(self) -> str:
        return super().__str__()



class Printer(models.Model):
    voucher_numberp = models.CharField(db_column='Voucher_Number', max_length=50, blank=True, default=None, primary_key=True)
    brand_name = models.CharField(db_column='Brand_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    model_name = models.CharField(db_column='Model_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    grant = models.CharField(db_column='Grant', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pyop = models.CharField(db_column='Year_Of_Purchase', blank=True, null=True,max_length=4)  # Field name made lowercase. This field type is a guess.
    ptype = models.CharField(db_column='Printer_Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    group = models.CharField(db_column='Group', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nomenclature = models.CharField(db_column='Nomenclature', max_length=250, blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'printer'

    def __str__(self) -> str:
        return super().__str__()


class Ups(models.Model):
    voucher_numberu = models.CharField(db_column='Voucher_Number', max_length=50, blank=True, default=None, primary_key=True)
    brand_name = models.CharField(db_column='Brand_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    model_name = models.CharField(db_column='Model_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    grant = models.CharField(db_column='Grant', max_length=50, blank=True, null=True)  # Field name made lowercase.
    uyop = models.CharField(db_column='Year_Of_Purchase', blank=True, null=True,max_length=4)  # Field name made lowercase. This field type is a guess.
    ups_power = models.CharField(db_column='UPS_Power', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ups_type = models.CharField(db_column='UPS_Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    group = models.CharField(db_column='Group', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nomenclature = models.CharField(db_column='Nomenclature', max_length=250, blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'ups'

    def __str__(self) -> str:
        return super().__str__()

class MultifunctionalDevice(models.Model):
    voucher_numberm = models.CharField(db_column='Voucher_Number', max_length=50, blank=True, default=None, primary_key=True)
    brand_name = models.CharField(db_column='Brand_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    model_name = models.CharField(db_column='Model_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    grant = models.CharField(db_column='Grant', max_length=50, blank=True, null=True)  # Field name made lowercase.
    purchaseyear = models.CharField(db_column='Year_Of_Purchase', blank=True, null=True,max_length=4)  # Change TextField to CharField
    group = models.CharField(db_column='Group', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nomenclature = models.CharField(db_column='Nomenclature', max_length=250, blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'multifunctional_device'

    def __str__(self) -> str:
        return super().__str__()


class LogoPic(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    pic = models.FileField()