from .models import UserProfile, User, CartItem, Order
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'gender','birthdate','image']

class UserRegisterForm(UserCreationForm):
   
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_superuser', 'is_staff' )


class CartItemForm(ModelForm):
    class Meta:
        model = CartItem
        fields = ['product', 'quantity']


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['payment_type']