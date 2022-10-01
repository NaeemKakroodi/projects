from django.shortcuts import render
from django.http import HttpResponse
#import requests


def home(request):

  return render(request,'home.html',{'name':'guy'})


def operate(request):
   val1 = float(request.POST.get('num1'))
   val2 = float(request.POST.get('num2')) 
   operation = request.POST['operation']
   if operation == '+': res = val1 + val2
   elif operation == '-': res = val1 - val2
   elif operation == '*': res = val1 * val2
   elif operation == '/': res = val1 / val2
   elif operation == '**': res = val1 ** val2

   return render(request,'resault.html', {'res': res})


