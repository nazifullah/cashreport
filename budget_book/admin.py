from django.contrib import admin
from .models import *

class ListCommitment(admin.ModelAdmin):
    list_display = ('amount','donorname','year')
    list_display_links = ('donorname',)

class ListOpeningBalance(admin.ModelAdmin):
    list_display = ('opening_amount','account_name','year')
    list_display_links = ('account_name',)


class ListReceivableAmount(admin.ModelAdmin):
    list_display = ('recieveable_amount','name','year')
    list_display_links = ('name',)


# Register your models here.
admin.site.register(Commitment, ListCommitment)
admin.site.register(Openingbalance, ListOpeningBalance)
admin.site.register(Receivable, ListReceivableAmount)
admin.site.register(Year)