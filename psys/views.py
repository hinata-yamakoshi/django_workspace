from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Customer

def Index(request):
    return render(request, 'customer/index.html')

def login(request):
    error_message = ''
    if request.method == "POST":
        employee_no = request.POST.get('employee_no')
        password = request.POST.get('password')
    return render(request, 'customer/Login.html', {'error_message':error_message})

def MainMenu(request):
    return render(request, 'customer/CustomerManagementMenu.html')

def CustomerSearch(request):
    customer_code = ''
    error_message = ''
    customer = None
    if request.method == "POST":
        customer_code = request.POST.get('customer_code')
        request.session['search_customer_code'] = customer_code
        return redirect('psys:CustomerSearch')
    else:
        customer_code = request.session.pop('search_customer_code',None)
        if customer_code:
            try:
                customer = Customer.objects.get(
                    customer_code=customer_code
                )
            except Customer.DoesNotExist:
                error_message = '該当する得意先コードは存在しません。'
    return render(request, 'customer/CustomerSearch.html', {'customer':customer,'error_message':error_message})