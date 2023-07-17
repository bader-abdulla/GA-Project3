from django.shortcuts import render, redirect
from django.core.mail import BadHeaderError, send_mail
from .models import UserProfile, Order,Cart, CartItem, ProductCategory,Customer , Product, User
from .forms import UserProfileForm, UserRegisterForm, CartItemForm, OrderForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    return render(request, 'home.html')


def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')




# UserProfile
class UserProfileList(LoginRequiredMixin, ListView):
    model = UserProfile
    paginate_by = 5

class UserProfileDetail(LoginRequiredMixin, DetailView):
    model = UserProfile

class UserProfileCreate(LoginRequiredMixin, CreateView):    
    model = UserProfile
    fields = ['phone_number', 'gender', 'birthdate', 'image']
        # Override 
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UserProfileUpdate(LoginRequiredMixin, UpdateView):
    model = UserProfile
    fields = ['phone_number', 'gender','birthdate','image']

class UserProfileDelete(LoginRequiredMixin, DeleteView):
    model = UserProfile
    success_url = '/'



# ProductCategory - @yousifnooh
class ProductCategoryList(LoginRequiredMixin, ListView):
    model = ProductCategory
    paginate_by = 5

class ProductCategoryDetail(LoginRequiredMixin, DetailView):
    model = ProductCategory

class ProductCategoryCreate(LoginRequiredMixin, CreateView):
    model = ProductCategory
    fields =['user', 'type','created_date', 'is_active']
    success_url = '/product-categories/'    

class ProductCategoryUpdate(LoginRequiredMixin, UpdateView):
    model = ProductCategory
    fields = ['type',  'is_active']
    success_url = '/product-categories/'    

class ProductCategoryDelete(LoginRequiredMixin, DeleteView):
    model = ProductCategory
    success_url = '/product-categories/'    



# Product - @bader-abdulla
class ProductList(LoginRequiredMixin, ListView):
    model = Product
    paginate_by = 5

class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product

class ProductCreate(LoginRequiredMixin, CreateView):    
    model = Product
    fields = ['name' , 'description' , 'price' , 'is_taxable' , 'image' , 'barcode' , 'is_active', 'product_category']

class ProductUpdate(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['name' , 'description' , 'price' , 'is_taxable' , 'image' , 'barcode' , 'is_active', 'product_category']

class ProductDelete(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = '/products/'



# Customer - @yousifnooh
class CustomerList(LoginRequiredMixin, ListView):
    model = Customer
    paginate_by = 5

class CustomerDetail(LoginRequiredMixin, DetailView):
    model = Customer

class CustomerCreate(LoginRequiredMixin, CreateView):
    model = Customer
    fields =['full_name', 'email', 'phone_number' ,'is_active']
    success_url = '/customers/'  
        # Override 
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)  

class CustomerUpdate(LoginRequiredMixin, UpdateView):
    model = Customer
    fields = ['user', 'full_name', 'email','is_active']
    success_url = '/customers/'    

class CustomerDelete(LoginRequiredMixin, DeleteView):
    model = Customer
    success_url = '/customers/'  



# Cart - @mahfood
class CartList(LoginRequiredMixin, ListView):
    model = Cart
    paginate_by = 5

class CartDetail(LoginRequiredMixin, DetailView):
    model = Cart

# Cart Create - - @salmanaljaziri
@login_required
def carts_detail(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cartItem_form = CartItemForm()
    order_form = OrderForm()
    items =CartItem.objects.filter(cart_id=cart_id)
    # owners_coin_dosnt_have = Owner.objects.exclude(id__in=coin.owners.all().values_list('id'))
    return render(request, 'carts/detail.html',{'cart': cart, 'cartItem_form': cartItem_form, 'cartItems': items, 'order_form': order_form})

@login_required
def add_cartItem(request, cart_id):
    form = CartItemForm(request.POST)
    if form.is_valid():
        new_cartItem = form.save(commit=False)
        new_cartItem.cart_id = cart_id
        new_cartItem.save()

    return redirect('carts_detail', cart_id = cart_id)

@login_required
def add_order(request, cart_id):
    form = OrderForm(request.POST)
    if form.is_valid():
        new_order = form.save(commit=False)
        print(new_order)
        new_order.cart_id = cart_id
        new_order.user_id = request.user.id
        new_order.save()
        cart =Cart.objects.get(id=cart_id)
        cart.is_closed = True
        cart.save()
    return redirect('orders_detail', pk = new_order.id)

class OrderList(LoginRequiredMixin, ListView):
    model = Order

class CartCreate(LoginRequiredMixin, CreateView):    
    model = Cart
    fields = ['customer']

    # Override 
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CartUpdate(LoginRequiredMixin, UpdateView):
    model = Cart
    fields = ['customer', 'is_closed']

class CartDelete(LoginRequiredMixin, DeleteView):
    model = Cart
    success_url = '/carts/'



# CartInfo - @mahfood
class CartItemList(LoginRequiredMixin, ListView):
    model = CartItem
    paginate_by = 5

class CartItemDetail(LoginRequiredMixin, DetailView):
    model = CartItem
    fields = ['quantity']

class CartItemCreate(LoginRequiredMixin, CreateView):
    model = CartItem
    fields = '__all__'
    # fields = ['quantity']

class CartItemUpdate(LoginRequiredMixin, UpdateView):
    model = CartItem
    fields = '__all__'
    # fields = ['quantity']

class CartItemDelete(LoginRequiredMixin, DeleteView):
    model = CartItem
    success_url = '/carts-details/'



# Order - @salmanaljaziri
class OrderList(LoginRequiredMixin, ListView):
    model = Order
    paginate_by = 5

class OrderDetail(LoginRequiredMixin, DetailView):
    model = Order

class OrderCreate(LoginRequiredMixin, CreateView):    
    model = Order
    fields = ['cart', 'order_status', 'payment_type', 'payment_status']
    # fields = '__all__'
        # Override 
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class OrderUpdate(LoginRequiredMixin, UpdateView):
    model = Order
    fields = ['cart', 'order_status', 'payment_type', 'payment_status']

class OrderDelete(LoginRequiredMixin, DeleteView):
    model = Order
    success_url = '/orders/'





def signup(request):
    error_message = ""
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            return redirect('userprofiles_index')
        else:
            error_message = "Invalid signup - Please try again later."
    
    form = UserRegisterForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


# def signin (request) :
#     return render (request , 'registration/login.html')

