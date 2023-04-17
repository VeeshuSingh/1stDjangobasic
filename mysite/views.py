# i have created this file.
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
     return render(request,'index.html')
def form(request):
     return render(request,'form.html')
def submit(request):
     djtext=request.POST.get('yht','default')
     cb=request.POST.get('cb','off')
     cb1=request.POST.get('cb1','default')
     removetext=request.POST.get('rt','default')

     if cb=="on":
          djtext=djtext.upper()
     if cb1=="on":
          l=djtext.split()
          c=''
          for i in l:
               print(removetext.upper())
               print(i.upper())
               if (i.upper())!=removetext.upper():
                    c=c+i+" "
          djtext=c
     params={'purpose':'your final text is','new_text':djtext,}
     return render(request ,'analyze.html',params)
     
