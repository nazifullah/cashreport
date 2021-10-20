from django.urls import path
from cash_report import views

app_name = 'cashreport'
urlpatterns=[

    path('DailyReport/', views.DailyReport, name='DailyReport'),
    path('export-csv', views.export_csv, name='export-csv'),
    path('export-pdf/', views.export_pdf, name='export-pdf'),
    path('export-excel/', views.export_excel, name='export-excel'),
    # path('commimtment/', views.savecommitment, name='savecommitment'),
    # path('opening-balance/', views.addopeningbalance, name='addopeningbalance'),
    # path('receivable-amount', views.addreceivableamount, name='addreceivableamount'),
    # path('year', views.addyear, name='addyear'),
]
