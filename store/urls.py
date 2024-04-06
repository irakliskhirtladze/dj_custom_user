from django.urls import path
from store import views


urlpatterns = [
    path('store', views.get_books, name='store_home'),
    path('store/<int:book_id>-book-details', views.get_book, name='book_details'),
    path('store/<int:book_id>-add-to-cart', views.add_to_cart, name='add_to_cart'),
    path('store/<int:book_id>-remove-from-cart', views.remove_from_cart, name='remove_from_cart'),
    path('store/cart', views.cart, name='cart'),
]
