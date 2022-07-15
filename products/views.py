from django.http import JsonResponse
from .serializers import ProductSerializer
from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

@api_view(("GET",))
def all_products(request):
    if request.method == "GET":
        all_products = Product.objects.all()
        serializer = ProductSerializer(all_products, many=True)
        return Response(serializer.data)

@api_view(("GET", "POST"))
def this_product(request, category, slug):

    # Try to get the product from the database, throw error if the product is not found
    try:
        product = Product.objects.get(slug=slug, category=category)
    except ObjectDoesNotExist:
        return JsonResponse({"error_message": "The product you seek does not exist."}, status=400)

    # Serialize and return the product to the user if it was a get request
    if request.method == "GET":
        serializer = ProductSerializer(product)
        return JsonResponse({"success_message": "Product Received Successfully", "product": serializer.data}, status=200)
        
        



# https://codeking12.github.io/Black-Hosting/
# https://codeking12.github.io/HosTechno/
