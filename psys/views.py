from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Customer

def index(request):
    return render(request, 'customer/index.html')

def customer_search(request):
    customer_code = ''
    error_message = ''
    customer = None
    if request.method == "POST":
        customer_code = request.POST.get('customer_code')
        try:
            customer = Customer.objects.get(
                customer_code=customer_code
            )
        except Customer.DoesNotExist:
            error_message = '該当する得意先コードは存在しません。'
    return render(request, 'customer/CustomerSearch.html', {'customer':customer,'error_message':error_message})