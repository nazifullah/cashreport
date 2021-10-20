from django.http import HttpResponse
from django.shortcuts import render
from jdatetime import date
from xlwt.Column import Column
from .models import Report
from budget_book.models import *
import datetime
import csv
import xlwt

from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from django.db.models import Sum
from jalali_date import datetime2jalali, date2jalali


# Create your views here.

def DailyReport(request):
    # queryset= Report.objects.all()
    testjalali = None
    if request.method == 'POST':
        queryset = Report.objects.filter(date=request.POST.get("date"))
        testdate = request.POST.get("date")[:4]
        print(request.POST.get("date"))
        year = convert_to_shamsi(request.POST.get("date"))
    else:
        queryset = Report.objects.all()
    openquerset = Openingbalance.objects.all()
    receivequeryset = Receivable.objects.all()
    commitqueryset = Commitment.objects.all()
    yearqueryset = Year.objects.all()
    recepitsqueryset = 6
    netReceiptsDonorGrants = queryset[0].donrgrntoptdev + \
        queryset[0].unspentgrnt
    TotalFundsAvailable = openquerset[1].opening_amount + recepitsqueryset
    grantsoperatingbudget = receivequeryset[1].recieveable_amount + receivequeryset[2].recieveable_amount + \
        receivequeryset[3].recieveable_amount + \
        receivequeryset[4].recieveable_amount
    opbudget = grantsoperatingbudget + \
        receivequeryset[0].recieveable_amount + \
        receivequeryset[5].recieveable_amount
    grantoperatingbudgetreceipts = queryset[0].frrlotfa + \
        queryset[0].frrctamod + queryset[0].frrctamoi + queryset[0].frrtdf
    opbugetreceips = grantoperatingbudgetreceipts + \
        queryset[0].totaldemrev + queryset[0].frrimfloan
    opbudgetbalance = opbudget - opbugetreceips
    demosticrevenuebalance = receivequeryset[0].recieveable_amount - \
        queryset[0].totaldemrev
    grantsopbdtbalance = grantsoperatingbudget - grantoperatingbudgetreceipts
    lotfabalance = receivequeryset[1].recieveable_amount - queryset[0].frrlotfa
    cstcamodbalance = receivequeryset[2].recieveable_amount - \
        queryset[0].frrctamod
    cstcamoibalance = receivequeryset[3].recieveable_amount - \
        queryset[0].frrctamoi
    tdfbalance = receivequeryset[4].recieveable_amount - queryset[0].frrtdf
    imfloanbalance = receivequeryset[5].recieveable_amount - \
        queryset[0].frrimfloan
    totalcommitment = commitqueryset[0].amount + commitqueryset[1].amount + \
        commitqueryset[2].amount + commitqueryset[3].amount
    totalexpenditure = commitqueryset[0].amount + queryset[0].freadb + \
        queryset[0].freusaid + queryset[0].freotherdonrs
    balanceartfwb = commitqueryset[0].amount - queryset[0].freartfwb
    balanceadb = commitqueryset[1].amount - queryset[0].freadb
    balanceusaid = commitqueryset[2].amount - queryset[0].freusaid
    balanceotherdonors = commitqueryset[3].amount - queryset[0].freotherdonrs
    totalbalance = balanceartfwb + balanceadb + balanceusaid + balanceotherdonors

    totalofopening = 0
    for i in openquerset:
        totalofopening += i.opening_amount

    context = {
        'queryset': queryset,
        'openquerset': openquerset,
        'receivequeryset': receivequeryset,
        'commitqueryset': commitqueryset,
        'yearqueryset': yearqueryset,
        'netReceiptsDonorGrants': netReceiptsDonorGrants,
        'TotalFundsAvailable': TotalFundsAvailable,
        'grantsoperatingbudget': grantsoperatingbudget,
        'opbudget': opbudget,
        'grantoperatingbudgetreceipts': grantoperatingbudgetreceipts,
        'opbugetreceips': opbugetreceips,
        'opbudgetbalance': opbudgetbalance,
        'demosticrevenuebalance': demosticrevenuebalance,
        'grantsopbdtbalance': grantsopbdtbalance,
        'lotfabalance': lotfabalance,
        'cstcamodbalance': cstcamodbalance,
        'cstcamoibalance': cstcamoibalance,
        'tdfbalance': tdfbalance,
        'imfloanbalance': imfloanbalance,
        'totalcommitment': totalcommitment,
        'totalofopening': totalofopening,
        'totalexpenditure': totalexpenditure,
        'balanceartfwb': balanceartfwb,
        'totalbalance': totalbalance,
        'balanceadb': balanceadb,
        'balanceusaid': balanceusaid,
        'balanceotherdonors': balanceotherdonors,
        'testdate': testdate,
        'testjalali': year



    }
    return render(request, 'cash_report/DailyReport.html', context)


def export_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=Expenses' +\
        str(datetime.datetime.now())+'.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    html_string = render_to_string(
        'cash_report/pdf-output.html', {'cashmanagements': [], 'total': 0})
    html = HTML(string=html_string)

    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())

    return response


def export_csv(request):
    response = HttpResponse(content_type='application/csv')
    response['Content-Disposition'] = 'attachment; filename=CashManagement' + \
        str(datetime.datetime.now())+'.csv'
    writer = csv.writer(response)
    writer.writerow(['revenue', 'totaldemrev', 'donrgrntoptdev'])
    # cashmanagements = Report.objects.filter(ownre=request.user)
    cashmanagements = Report.objects.all()

    for cashmanagement in cashmanagements:
        writer.writerow(
            [cashmanagement.revenue, cashmanagement.totaldemrev, cashmanagement.donrgrntoptdev])
    return response


def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=CashManagement' + \
        str(datetime.datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('CashManagement')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['revenue', 'totaldemrev', 'donrgrntoptdev']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
        font_style = xlwt.XFStyle()
        # rows = Report.objects.filter(owner=request.user).values_list('revenue','totaldemrev','donrgrntoptdev')
        rows = Report.objects.all().values_list(
            'revenue', 'totaldemrev', 'donrgrntoptdev')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response


def convert_to_shamsi(date):
    date_list = date.split("-")
    year = int(date_list[0])
    month = int(date_list[1])
    day = int(date_list[2])
    result = None
    if month <= 3:
        if month == 3 and day in range(1, 21):
            result = year - 622
            print("1")
        elif month < 3:
            result = year - 622
            print("2")
        elif month == 3 and day in range(21, 32):
            result = year - 621
            print("3")
    else:
        result = year - 621
        print("4")
    return result
