from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="login", permanent=False), name="root"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("guest/", views.guest_login_view, name="guest_login"),
    path("products/", views.product_list, name="product_list"),
    path("products/add/", views.product_add, name="product_add"),
    path("products/<int:pk>/edit/", views.product_edit, name="product_edit"),
    path("products/<int:pk>/delete/", views.product_delete, name="product_delete"),
    path("orders/", views.order_list, name="order_list"),
    path("orders/<int:pk>/edit/", views.order_edit, name="order_edit"),
    path("orders/<int:pk>/delete/", views.order_delete, name="order_delete"),
]
