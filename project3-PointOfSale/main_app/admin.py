from django.contrib import admin
# from django.contrib.auth.models import User,Group
from .models import UserProfile,ProductCategory,Customer,Order,Cart,CartItem,Product

# admin.site.unregister(Group)
# admin.site.unregister(User)

# Register your models here.
@admin.action(description="Print")
def print_action(modeladmin, request, queryset):
    print(queryset)


class CustomerAdmin(admin.ModelAdmin):
    # model = Customer
    list_display = ('full_name','email','phone_number')
    search_fields = ('full_name','email','phone_number')
    list_per_page = 5

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','description','product_category') 
    search_fields = ('name','description','product_category')
    list_filter = ('product_category',)
    ordering = ('name',)
    actions = [print_action]
    list_per_page = 5
    # readonly_fields = ['description']

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','phone_number','birthdate') 
    search_fields = ('user','phone_number','birthdate')
    list_filter = ('user',)
    ordering = ('user',)
    actions = [print_action]
    list_per_page = 5

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','payment_type','order_status') 
    search_fields = ('user','order_status')
    list_filter = ('order_status',)
    ordering = ('user',)
    actions = [print_action]
    list_per_page = 5   

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product','quantity') 
    search_fields = ('product','quantity')
    list_filter = ('product',)
    ordering = ('cart',)
    actions = [print_action]
    list_per_page = 5  


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('type','created_date','is_active') 
    search_fields = ('type','created_date','is_active')
    list_filter = ('type',)
    ordering = ('type',)
    actions = [print_action]
    list_per_page = 5

class CartAdmin(admin.ModelAdmin):
    list_display = ('customer','cart_date')
    search_fields = ('customer','cart_date')
    list_filter = ('customer',)
    ordering = ('customer',)
    actions = [print_action]
    list_per_page = 5


# UserProfile @salmanalajziri
admin.site.register(UserProfile,UserProfileAdmin),
# ProductCategory - @yousifnooh
admin.site.register(ProductCategory,ProductCategoryAdmin),

# Product - @bader-abdulla
admin.site.register(Product,ProductAdmin)

# Customer - @yousifnooh
admin.site.register(Customer, CustomerAdmin),


# Cart - @mahfood
admin.site.register(Cart,CartAdmin)

# CartDetail - @mahfood
admin.site.register(CartItem,CartItemAdmin)

# Order - @salmanalajziri
admin.site.register(Order,OrderAdmin)



