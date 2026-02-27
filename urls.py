from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='shop/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='shop:home'), name='logout'),
]