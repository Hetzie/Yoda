from django.shortcuts import render
from .models import Person


# Create your views here.
# def index(request):
#     return render(request, 'new.html')

def index(request):
    query = Person.objects.all()
    return render(request, 'new.html', {'data':query})

def button(request):
    data = request.GET.get('name')
    return render(request, 'result.html', {'data':data})