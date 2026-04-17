from django.shortcuts import render,redirect
from testapp.models import employee
from testapp.forms import empform

# Create your views here.
def retrive(request):
    emp=employee.objects.all()
    return render(request,'index.html',{'emp':emp})

def insert(request):
    form=empform()
    if request.method=='POST':
        form=empform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/retrive/')
            
    return render(request,'insert.html',{'form':form})


def delete(request,id):
    emp=employee.objects.get(id=id)
    emp.delete()
    return redirect('/retrive/')


def update(request,id):
    emp=employee.objects.get(id=id)
    form=empform(instance=emp)

    if request.method == 'POST':
        form = empform(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            return redirect('/retrive/')
    return render(request,'update.html',{'form':form})
