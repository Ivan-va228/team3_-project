from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from products.models import Product
from brands.models import Brand
from categories.models import Category

def home(request):
    products1 = Product.objects.all()[:16]
    products2 = Product.objects.all()[:10]
    return render(request, 'home.html', {
        'products1': products1,
        'products2': products2
    })

def catalog(request):
    products = Product.objects.all()
    brands = Brand.objects.all()
    categories = Category.objects.all()

    selected_brands = request.GET.getlist('brand')
    selected_categories = request.GET.getlist('category')
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    rating_min = request.GET.get('rating_min')

    if selected_brands:
        products = products.filter(brand_id__in=selected_brands)
    if selected_categories:
        products = products.filter(category__in=selected_categories)
    if price_min:
        products = products.filter(price__gte=price_min)
    if price_max:
        products = products.filter(price__lte=price_max)
    if rating_min:
        products = products.filter(rating__gte=rating_min)

    context = {
        'products': products,
        'brands': brands,
        'categories': categories,
        'selected_brands': selected_brands,
        'selected_categories': selected_categories,
        'price_min': price_min,
        'price_max': price_max,
        'rating_min': rating_min,
    }
    return render(request, 'catalog.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})

    price = float(product.price) 
    image_url = product.image.url if product.image else None  
    
    if str(product_id) not in cart:
        cart[str(product_id)] = {
            'name': product.name,
            'price': price,  
            'quantity': 1,
            'image_url': image_url 
        }
    else:
        cart[str(product_id)]['quantity'] += 1
    
    request.session['cart'] = cart
    
    return redirect(request.META.get('HTTP_REFERER'))


def update_cart(request, product_id):
    action = request.POST.get('action')
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        if action == 'increase':
            cart[str(product_id)]['quantity'] += 1  
        elif action == 'decrease':
            if cart[str(product_id)]['quantity'] > 1:
                cart[str(product_id)]['quantity'] -= 1  
            else:
                del cart[str(product_id)] 

    request.session['cart'] = cart
    return redirect('cart')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        del cart[str(product_id)] 

    request.session['cart'] = cart
    return redirect('cart')

def cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    for item_id, item_data in cart.items():
        if item_id:
            item_data['id'] = item_id
            cart_items.append(item_data)
            total += item_data['price'] * item_data['quantity'] 

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })

def search_products(request):
    query = request.GET.get('q', '').lower()
    if not query:
        return JsonResponse({'count': 0, 'results': []})

    products = Product.objects.filter(Q(name__icontains=query)).distinct()
    results = []

    for product in products:
        product_url = f"/product/{product.id}/"
        results.append({
            'name': product.name,
            'price': product.price,
            'image_url': product.image.url if product.image else None,
            'product_url': product_url,
        })

    return JsonResponse({'count': len(results), 'results': results})

def like(request):
    return render(request, 'like.html')

def account(request):
    return render(request, 'user.html')

def register(request):
    return render(request, 'register.html')
