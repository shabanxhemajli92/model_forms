from django.shortcuts import render
from .forms import CustomerForm

def index(request):
    form = CustomerForm()
    
    if request.method =="POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'/home/dci-admin/Desktop/model_forms/mysite/customer/templates/index.html',context)