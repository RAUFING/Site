from django.shortcuts import render
from django.http import HttpResponse
import random

from .forms import MagicOne, MagicTwo, MagicThree
num = '3'
# Create your views here.
def index(request):
    global num
    #num = str(random.randint(1, 100))
    return render(request,'index.html')
def game(request):
    global num
    num = int(num)
    
    if request.method == 'POST':
        form1 = int(request.POST.get('form1'))
        form2 = int(request.POST.get('form2'))
        form3 = int(request.POST.get('form3'))
        form4 = int(request.POST.get('form4'))
        form5 = int(request.POST.get('form5'))
        form6 = int(request.POST.get('form6'))
        form7 = int(request.POST.get('form7'))
        form8 = int(request.POST.get('form8'))
        form9 = int(request.POST.get('form9'))
        if (form1 + form2 + form3) == num \
        and (form4 + form5 + form6) == num \
        and (form7 + form8 + form9) == num \
        and (form1 + form4 + form7) == num \
        and (form2 + form5 + form8) == num \
        and (form3 + form6 + form9) == num \
        and (form1 + form5 + form9) == num \
        and (form3 + form5 + form7) == num:
            return render(request, 'finishTrue.html')
        else:
            return render(request, 'finishFalse.html')
    else:
        mag1 = MagicOne()
        mag2 = MagicTwo()
        mag3 = MagicThree()
        num = str(num)
        data = {'form1':mag1, 'form2':mag2, 'form3':mag3, 'num':num}
        
        return render(request, 'game.html', context=data)