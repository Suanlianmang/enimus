from django.urls import path
from .views import main, customer_signup, seller_signup

urlpatterns = [
	path('', main, name='main'),
	path('signup/customer', customer_signup, name='csignup'),
	path('signup/seller', seller_signup, name='ssignup'),
]