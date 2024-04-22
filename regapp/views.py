from django.shortcuts import render
from django.views import View
class Home(View):
    def get(self,request):
        return render(request,'reginput.html')
class Verify(View):
    def get(self,request):
        con_dict={"t1":request.GET["t1"],
                  "t2":request.GET["t2"],
                  "t3":request.GET["t3"],
                  "t6":request.GET["t6"],
                  "t7":request.GET["t7"],
                  }
        return render(request,'verify.html',context=con_dict)