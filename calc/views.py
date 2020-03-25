from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
     return render(request,'home.html',{'name':'upabupa'})
     
def result(request):
     #val1 = int(request.POST.get("num1"))
     #val2 = int(request.POST.get("num2"))
     
     val1 = int(request.POST["num1"])
     val2 = int(request.POST["num2"])
     
     res = val1 + val2
     
     return render(request,'result.html',{"res":res})
