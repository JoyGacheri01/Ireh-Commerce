from django.shortcuts import render, redirect, get_object_or_404
from .models import Slider, About, New_Arrival, Best_sellers, Discounted, Message, Cleansing, Oil, Treatment, Braiding
from . models import Product, CartItem
from django.db.models import Q




# Create your views here.
def index(request):
    sliders = Slider.objects.all()
    about = About.objects.all()
    new_arrival = New_Arrival.objects.all()
    best_sellers = Best_sellers.objects.all()
    discounted = Discounted.objects.all()
    return render(request, 'index.html', {
        'sliders': sliders, 
        'abouts': about, 
        'new_arrival': new_arrival,
        'best_sellers': best_sellers,
        'discounted': discounted,
        })

def about(request):
    return render(request, "about.html")

def product(request):
    cleansing = Cleansing.objects.all()
    oil = Oil.objects.all()
    treatment = Treatment.objects.all()
    braiding = Braiding.objects.all()
    return render(request, "product.html", {'cleansing': cleansing, 'oil': oil, 'treatment':treatment, 'braiding':braiding})

def cart(request):
    return render(request, "cart.html")

def services(request):
    return render(request, "service-details.html")

def insert_message(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        new_message = Message(
            name = name,
            email = email,
            subject = subject,
            message=message
            
        )
        new_message.save()
        message.success(request, "Thank you for contacting us! We will get back to you soon.")
        return redirect('/')
    
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})

def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price* item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart/')

def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('product/')

def search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'search.html', {'results': results, 'query': query})



