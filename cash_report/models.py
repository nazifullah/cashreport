from datetime import date
from django.db import models
from budget_book.models import Year
from jalali_date import date2jalali, datetime2jalali
# Create your models here.


class Report(models.Model):
    revenue = models.DecimalField(max_digits=18, decimal_places=2)
    totaldemrev = models.DecimalField(max_digits=18, decimal_places=2)
    donrgrntoptdev = models.DecimalField(max_digits=18, decimal_places=2)
    unspentgrnt = models.DecimalField(max_digits=18, decimal_places=2)
    otherreceipts = models.DecimalField(max_digits=18, decimal_places=2)
    trddbe = models.DecimalField(max_digits=18, decimal_places=2)
    totrbexpenditure = models.DecimalField(max_digits=18, decimal_places=2)
    batab = models.DecimalField(max_digits=18, decimal_places=2,)
    batar = models.DecimalField(max_digits=18, decimal_places=2)
    bauspenta = models.DecimalField(max_digits=18, decimal_places=2)
    baexpenditure = models.DecimalField(max_digits=18, decimal_places=2)
    frrlotfa = models.DecimalField(max_digits=18, decimal_places=2)
    frrctamod = models.DecimalField(max_digits=18, decimal_places=2)
    frrctamoi = models.DecimalField(max_digits=18, decimal_places=2)
    frrtdf = models.DecimalField(max_digits=18, decimal_places=2)
    frrimfloan = models.DecimalField(max_digits=18, decimal_places=2)
    frrcashreverse = models.DecimalField(max_digits=18, decimal_places=2)
    frreroupcommission = models.DecimalField(max_digits=18, decimal_places=2)
    frreroupcomrefugee = models.DecimalField(max_digits=18, decimal_places=2)
    frrusdevaids = models.DecimalField(max_digits=18, decimal_places=2)
    frrartfip = models.DecimalField(max_digits=18, decimal_places=2)
    freartfwb = models.DecimalField(max_digits=18, decimal_places=2)
    freadb = models.DecimalField(max_digits=18, decimal_places=2)
    freusaid = models.DecimalField(max_digits=18, decimal_places=2)
    freotherdonrs = models.DecimalField(max_digits=18, decimal_places=2)
    year = models.ForeignKey(
        Year, on_delete=models.DO_NOTHING, related_name="report")
    date = models.DateField()

    def __str__(self):
        return self.revenue
