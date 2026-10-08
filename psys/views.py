from django.shortcuts import render

# Create your views here.
def customer_search(request):
    return render(request, 'customer/CustomerSearch.html')