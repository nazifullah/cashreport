from os import name
from django.shortcuts import render
from django.http import HttpResponse
from .models import Year, Commitment, Openingbalance, Receivable

# Create your views here.
def index(request):
    
    # return HttpResponse('Cashmanagement')
    return render(request, 'budget_book/index.html')

def displaycommitment(request):
    # return HttpResponse('Cashmanagement')
    queryset = Year.objects.all()
    context={
        'years': queryset
    }
    return render(request, 'budget_book/commitment.html', context)
# def savecommitment(request):
#     # return HttpResponse('Cashmanagement')
#     queryset = Year.objects.all()
#     context={
#         'years': queryset
#     }
#     return render(request, 'budget_book/commitment.html', context)


def savecommitment(request):
    if request.method == 'POST':
        amount = request.POST['amount']
        donorname = request.POST['donername']
        year_id = request.POST['year']

        year = Year.objects.get(id=year_id)

        commitment = Commitment.objects.create(amount=amount, donorname=donorname, year=year)
        commitment.save()
    
    
    return render(request, 'budget_book/commitment.html')


def displayopeningbalance(request):
    return render(request, 'budget_book/openingbalance.html')

def displayreceivableamount(request):
    return render(request, 'budget_book/receiveble.html')

def displayyear(requst):
    return render(requst, 'budget_book/year.html')

def addopeningbalance(request):
    if request.method == 'POST':
        opening_amount = request.POST['openingamount']
        account_name = request.POST['accountname']
        year_id =request.POST['year']
        year = Year.objects.get(id=year_id)
        openingbalance = Openingbalance.objects.create(opening_amount=opening_amount, account_name=account_name, year=year)
        openingbalance.save()
         
    return render(request, 'budget_book/openingbalance.html')

def addreceivableamount(request):
    if request.methode =='POST':
       recieveable_amount = request.POST['recieveable_amount']
       name = request.POST['name']
       year_id = request.POST['year']
       year = Year.objects.get(id=year_id)     
       receivableamount = Receivable.objects.create(recieveable_amount=recieveable_amount, name=name, year=year)
       receivableamount.save()
    return render(request, 'budget_book/receiveble.html')

def addyear(requst):
    if requst.method == 'POST':
        year = requst.POST['year']
        yearadd= Year.objects.create(year=year)
        yearadd.save() 
    return render(requst, 'budget_book/year.html')

