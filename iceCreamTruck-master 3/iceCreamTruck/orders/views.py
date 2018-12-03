from django import forms
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse

from django.utils import timezone
from .models import OrderForm
from .forms import OrderModelForm

def index(request):
    latest_order_list = OrderForm.objects.order_by('-current_date')[:5]
    context = {'latest_order_list':latest_order_list}
    return render(request,'orders/index.html',context)
def detail(request, order_id):
    order = get_object_or_404(OrderForm, pk=order_id)
    return render(request,'orders/detail.html',{'order':order})
def results(request, order_id):
    response = "You're looking at the results of the order %s."
    return HttpResponse(response % order_id)
def input(request):
    if  request.method == "Post":
        form = OrderModelForm(request.POST)
        if form.is_valud():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/')
    else:
        form= OrderModelForm()
        return render(request,'orders/inputPage.html',{'form':form})
        

    
    return render(request,'orders/inputPage.html')
def vote(request, order_id):
    return HttpResponse("You're voting on question %s." % order_id)
