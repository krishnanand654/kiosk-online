from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "orders"

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_request, name="login"),
    path("register/", views.register, name="register"),
    path("logout", views.logout_request, name="logout"),
    path("Pizza", views.pizza, name="pizza"),
    path("Drinks", views.drink, name="drink"),
    path("Payments", views.payment, name="payment"),
    path("Snacks", views.snack, name="snack"),
    path("Subs", views.subs, name="subs"),
    path("Platters", views.dinner_platters, name="dinner_platters"),
    path("directions", views.directions, name="directions"),
    path("hours", views.hours, name="hours"),
    path("contact", views.contact, name="contact"),
    path("cart", views.cart, name="cart"),
    path("checkout", views.checkout, name="checkout"),
    path("view-orders", views.view_orders, name="view_orders"),
    path("mark_order_as_delivered", views.mark_order_as_delivered, name="mark_order_as_delivered"),
    path("save_cart", views.save_cart, name="save_cart"),
    path("retrieve_saved_cart", views.retrieve_saved_cart, name="retrieve_saved_cart"),
    path("check_superuser", views.check_superuser, name="check_superuser"),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

