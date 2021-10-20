
from django.db import models

# Create your models here.
class Year(models.Model):
    fiscal_year = models.IntegerField() 
    def __str__(self):
     return str(self.fiscal_year)
   

class Commitment(models.Model):
    amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=2)  
    donorname = models.TextField(db_column='DonorName', blank=True, null=True)  
    year = models.ForeignKey(Year, on_delete=models.DO_NOTHING, related_name="commitment")

    def __str__(self):
     return str(self.amount)


   


class Openingbalance(models.Model):
    opening_amount = models.DecimalField(max_digits=18, decimal_places=2)  
    account_name = models.CharField(max_length=200)  
    year = models.ForeignKey(Year, on_delete=models.DO_NOTHING, related_name="openingbalance")

    def __str__(self):
        return str(self.opening_amount)



class Receivable(models.Model):
    recieveable_amount = models.DecimalField(max_digits=18, decimal_places=2) 
    name = models.TextField(blank=True, null=True)  
    year = models.ForeignKey(Year, on_delete=models.DO_NOTHING, related_name="receivable")

    def __str__(self):
        return str(self.recieveable_amount),self.name