from django.contrib import admin
from django.contrib.admin.sites import site
from .models import *
# Register your models here.
admin.site.site_header = "Cash Management"
admin.site.register(Report)
