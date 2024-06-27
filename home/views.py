from django.shortcuts import render
from.forms import Aforms
from .models import Amodel

def add(request):
    if request.method=='POST':
        fm= Aforms(request.POST)
        if fm.is_valid():
            fm.save()
        fm=Aforms()

    else:
        fm=Aforms()
    stu=Amodel.objects.all() 

    return render(request, 'add.html', {'fm': fm, 'stu':stu})