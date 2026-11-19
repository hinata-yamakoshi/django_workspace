from django.shortcuts import render, redirect
from .models import Customer, Employee
from functools import wraps

def login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        employee_no = request.session.get('employee_no')
        if not employee_no:
            return redirect('psys:Login')
        return view_func(request, *args, **kwargs)
    return wrapper

def Index(request):
    return render(request, 'customer/index.html')

def login(request):
    error_message = ''
    if request.method == "POST":
        employee_no = request.POST.get('employee_no')
        password = request.POST.get('password')
        if not employee_no or not password:
            request.session['login_error'] = "従業員番号とパスワードを入力してください。"
            return redirect('psys:Login')
        else:
            try:
                employee = Employee.objects.get(
                    employee_no=employee_no,
                    password=password
                )
                request.session['employee_no'] = employee.employee_no
                return redirect('psys:MainMenu')
            except Employee.DoesNotExist:
                request.session['login_error'] = "従業員番号またはパスワードが間違っています。"
                return redirect('psys:Login')
    else:
        error_message = request.session.pop('login_error','')
    return render(request, 'customer/Login.html', {'error_message':error_message})

@login_required
def MainMenu(request):
    return render(request, 'customer/MainMenu.html')

@login_required
def CustomerManagementMenu(request):
    return render(request, 'customer/CustomerManagementMenu.html')

@login_required
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

def logout(request):
    request.session.flush()
    return redirect('psys:Index')