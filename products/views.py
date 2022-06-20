from django.shortcuts import render

# Create your views here.
def all_products(request):
    return render(request, "products/all-products.html")

def this_product(request):
    pass