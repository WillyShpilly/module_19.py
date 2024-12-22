from django.urls import path
from task1.views import main_page, shop, shopping_cart, sign_up_by_django

urlpatterns = [
        path('', main_page),
        path('games/', shop),
        path('cart/', shopping_cart),
        path('regdj/', sign_up_by_django)
]