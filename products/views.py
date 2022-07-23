from django.http import Http404, HttpResponse, JsonResponse
from .serializers import ProductSerializer
from products.models import Game, Product, ProductReviews, MoreProductImages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from django.shortcuts import redirect, render
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType

category_mapping = {"laptops": "pc", "phones": "phone", "games": "game"}

@api_view(("GET", "POST"))
def all_products(request):
    if request.method == "GET":
        all_products = Product.objects.all()
        serializer = ProductSerializer(all_products, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse({"data": request.POST}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(("GET", "PUT"))
def this_product(request, category_url, slug):

    # Try to get the product from the database, throw error if the product is not found
    try:
        product = Product.objects.get(slug=slug, category_url=category_url)
    except ObjectDoesNotExist:
        # return JsonResponse({"error_message": "The product you seek does not exist."}, status=400)
        return Response({"error_message": "The product you seek does not exist."}, status=status.HTTP_404_NOT_FOUND)

    # Serialize and return the product to the user if it was a get request
    if request.method == "GET":
        serializer = ProductSerializer(product)
        return Response({"success_message": "Product Found", "product": serializer.data}, status=status.HTTP_202_ACCEPTED)
        # return JsonResponse({"success_message": "Product Found", "product": serializer.data}, status=200)
        
def product_details(request, category_url, slug):
    try:
        product = Product.objects.get(slug=slug, category_url=category_url)
    except ObjectDoesNotExist:
        raise Http404
        # return redirect("home")
    
    extra_images = MoreProductImages.objects.filter(product=product)
    print(extra_images)
    related_products = Product.objects.filter(Q(category=product.category)) # | Q(details__manufacturer=product.details.manufacturer)
    return render(request, "products/product-details.html", {"product": product, "extra_images": extra_images, "related_products": related_products})

def product_group(request, category_url, field, field_value):
    category = category_mapping[category_url]
    field_model = ContentType.objects.get(app_label="products", model=category)
    field_products = field_model.get_all_objects_for_this_type(manufacturer__icontains=field_value.upper())
    print(field_products)
    # return HttpResponse(manufacturer_products)
    page_heading = f"{field_value} {category_url}".upper()
    return render(request, "products/product_field.html", {"field_products": field_products, "heading": page_heading})

def products_category(request, category_url):
    category = category_mapping[category_url]
    category_products = Product.objects.filter(category__icontains=category)
    return render(request, "products/category.html", {"category_products": category_products})

def search_products(request):
    return HttpResponse("Hello")

def game_franchises(request, franchise_name):
    field_products = Game.objects.filter(product__name__icontains=franchise_name)
    page_heading = f"{franchise_name} Franchise".upper()
    return render(request, "products/product_field.html", {"field_products": field_products, "heading": page_heading})

# https://codeking12.github.io/Black-Hosting/
# https://codeking12.github.io/HosTechno/
