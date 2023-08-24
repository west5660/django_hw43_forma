from django.shortcuts import render
from django.http import HttpResponse
from anketa.forms123 import Nashaforma2
# Create your views here.
def index(req):
    return render(req, 'index.html')
from anketa.forms123 import Nashaforma
from anketa.forms123 import Nashaforma2
def forma1(req):
    if req.method=='POST':
        name = req.POST.get('name')
        num = req.POST.get('num')
        output= '''<h1>Спасибо</h1> 
        <h2> Ваше имя -- {0} </h2>
        <h2> Ваше число -- {1} </h2>'''.format(name,num)
        return HttpResponse(output)
    else:
        anketa1=Nashaforma()
        data={'form':anketa1}
        return render(req,'forma.html',context=data)



def forma2(req):
    if req.method == 'POST':
        form = Nashaforma2(req.POST, req.FILES)
        name = req.POST.get('name')
        age = req.POST.get('age')
        poroda = req.POST.get('poroda')
        color = req.POST.get('color')
        food = req.POST.get('food')
        foto = req.FILES.get('foto')
        output = '''<h1>Спасибо</h1> 
           <h2> Ваше имя -- {0} </h2>
           <h2> Возраст -- {1} </h2>
           <h2>Порода -- {2}</h2>
           <h2>Цвет -- {3}</h2>
           <h2>Любимая еда -- {4}</h2>
           <h2>Фото --{5}</h2>'''.format(name, age, poroda, color, food, foto)
        context = {'name': name,'age': age,'poroda': poroda,'color': color,'food': food,'foto': foto,}
        return render(req, 'final.html', context)
    else:
        anketa1 = Nashaforma2()
        data = {'form': anketa1}
        return render(req, 'forma.html', context=data)


