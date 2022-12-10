from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
# Create your views here.
def index(request,param):

    mydata = Product.objects.all().values()
    print(mydata)
    return render(request ,'order/order.html',{'data': mydata})