from django import urls
from django.urls import path
from budget_book import views

app_name = 'dashboard'
urlpatterns=[

    path('', views.index, name='index'),
    path('commimtment/', views.displaycommitment, name='savecommitment'),
    path('opening-balance/', views.displayopeningbalance, name='addopeningbalance'),
    path('receivable-amount', views.displayreceivableamount, name='addreceivableamount'),
    path('year', views.displayyear, name='addyear'),
    path('save-commitment/', views.savecommitment, name='save_commit'),
    path('save-year/', views.addyear, name='save_year'),
    path('save-receivableamount/', views.addreceivableamount, name='save_receive'),
    path('save-openingbalance/', views.addopeningbalance, name='save_openbalance'),
]