from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from ecommerce.models import *
# Create your views here.
def ecommerce_index_view(request):
    '''This function render index page of ecommerce views'''

    return HttpResponse('Welcome to 6510742346 Natnicha Chokesuwattanaskul views!')

def item_view(request, item_id):
    context_data = {
        "item_id": item_id
    }
    return render(request, 'index.html',context = context_data)

def customer_all_view(request):
 customers = list(Customer.objects.all().values())
 return JsonResponse(customers, safe=False)