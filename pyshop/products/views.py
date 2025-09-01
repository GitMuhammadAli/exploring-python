from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

def all_options(request):
    return render(request, "products/all_option.html")

# List all products
def product_list(request):
    products = Product.objects.all()
    return render(request, "products/product_list.html", {"products": products})

# View single product
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "products/product_detail.html", {"product": product})

# Create product
def product_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        stock = request.POST.get("stock")

        Product.objects.create(
            name=name, description=description, price=price, stock=stock
        )
        return redirect("product_list")  # ✅ fixed
    return render(request, "products/product_form.html")

# Update product
def product_update(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        product.name = request.POST.get("name")
        product.description = request.POST.get("description")
        product.price = request.POST.get("price")
        product.stock = request.POST.get("stock")
        product.save()
        return redirect("product_detail", product_id=product.id)  # ✅ fixed

    return render(request, "products/product_form.html", {"product": product})

# Delete product
def product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        product.delete()
        return redirect("product_list")  # ✅ fixed
    return render(request, "products/product_confirm_delete.html", {"product": product})
