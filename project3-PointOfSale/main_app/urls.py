from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView

urlpatterns = [
    path('', views.home, name='index'),
    # path('accounts/change-password', PasswordChangeView.as_view(template_name='registration/change_password.html', success_url = '/'), name='change_password'), 
    path('accounts/password_change/', PasswordChangeView.as_view(template_name='registration/change-password.html'), name='password_change'),   
    path('reset-password', PasswordResetView.as_view(html_email_template_name='registration/password_reset_email.html'), name='password_reset'), 
    path('reset-password/done', PasswordResetDoneView.as_view(), name='password_reset_done'), 
    path('reset-password/confirm/<uidb64>[0-9A-Za-z]+)-<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'), 
    path('reset-password/complete/',PasswordResetCompleteView.as_view(),name='password_reset_complete'),


    path('accounts/signup/', views.signup, name='signup'),
    # path('', views.signin, name='signin'),



# UserProfile - @salmanaljaziri
    path('userprofiles/', views.UserProfileList.as_view(), name='userprofiles_index'),
    path('userprofiles/<int:pk>', views.UserProfileDetail.as_view(), name='userprofiles_detail'),
    path('userprofiles/<int:pk>/update/', views.UserProfileUpdate.as_view(), name='userprofiles_update'),
    path('userprofiles/create/', views.UserProfileCreate.as_view(), name='userprofiles_create'),
    path('userprofiles/<int:pk>/delete/', views.UserProfileDelete.as_view(), name='userprofiles_delete'),


# ProductCategory - @yousifnooh
    path('product-categories/', views.ProductCategoryList.as_view(), name='product_categories_index'),
    path('product-categories/<int:pk>', views.ProductCategoryDetail.as_view(), name='product_categories_detail'),
    path('product-categories/<int:pk>/update/', views.ProductCategoryUpdate.as_view(), name='product_categories_update'),
    path('product-categories/create/', views.ProductCategoryCreate.as_view(), name='product_categories_create'),
    path('product-categories/<int:pk>/delete/', views.ProductCategoryDelete.as_view(), name='product_categories_delete'),




# Product - @bader-abdulla
    path('products/', views.ProductList.as_view(), name='products_index'),
    path('products/<int:pk>', views.ProductDetail.as_view(), name='products_detail'),
    path('products/<int:pk>/update/', views.ProductUpdate.as_view(), name='products_update'),
    path('products/create/', views.ProductCreate.as_view(), name='products_create'),
    path('products/<int:pk>/delete/', views.ProductDelete.as_view(), name='products_delete'),



# Customer - @yousifnooh
    path('customers/', views.CustomerList.as_view(), name='customers_index'),
    path('customers/<int:pk>', views.CustomerDetail.as_view(), name='customers_detail'),
    path('customers/<int:pk>/update/', views.CustomerUpdate.as_view(), name='customers_update'),
    path('customers/create/', views.CustomerCreate.as_view(), name='customers_create'),
    path('customers/<int:pk>/delete/', views.CustomerDelete.as_view(), name='customers_delete'),




# Cart - @mahfood
    path('carts/', views.CartList.as_view(), name='carts_index'),
    path('carts/<int:cart_id>', views.carts_detail, name='carts_detail'),
    path('carts/<int:pk>/update/', views.CartUpdate.as_view(), name='carts_update'),
    path('carts/create/', views.CartCreate.as_view(), name='carts_create'),
    path('carts/<int:pk>/delete/', views.CartDelete.as_view(), name='carts_delete'),
    path('carts/<int:cart_id>/add_cartItem', views.add_cartItem, name='add_cartItem'),
    path('carts/<int:cart_id>/add_order', views.add_order, name='add_order'),





# CartItem - @mahfood
    path('cart-items/', views.CartItemList.as_view(), name='cart_items_index'),
    path('cart-items/<int:pk>', views.CartItemDetail.as_view(), name='cart_items_detail'),
    path('cart-items/<int:pk>/update/', views.CartItemUpdate.as_view(), name='cart_items_update'),
    path('cart-items/create/', views.CartItemCreate.as_view(), name='cart_items_create'),
    path('cart-items/<int:pk>/delete/', views.CartItemDelete.as_view(), name='cart_items_delete'),




# Order - @salmanaljaziri
    path('orders/', views.OrderList.as_view(), name='orders_index'),
    path('orders/<int:pk>', views.OrderDetail.as_view(), name='orders_detail'),
    path('orders/<int:pk>/update/', views.OrderUpdate.as_view(), name='orders_update'),
    path('orders/create/', views.OrderCreate.as_view(), name='orders_create'),
    path('orders/<int:pk>/delete/', views.OrderDelete.as_view(), name='orders_delete'),


]