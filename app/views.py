from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')
def create(request):
    return render(request, 'create.html')
def store(request):
    data={}
    if(request.POST['password'] != request.POST['password-confirm']):
        data['msg']="senha e confirmação diferentes"
        data['class']="alert-danger"
    return render(request, 'create.html', data)
