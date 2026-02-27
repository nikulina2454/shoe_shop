from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Order, Product
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Логин (email)",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите email",
                "autofocus": True,
            }
        ),
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите пароль",
            }
        ),
    )


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "article",
            "name",
            "unit",
            "price",
            "discount_percent",
            "stock_quantity",
            "description",
            "image_file",
            "category",
            "manufacturer",
            "supplier",
        ]
        widgets = {
            "article": forms.TextInput(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "unit": forms.Select(attrs={"class": "form-select"}),
            "price": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "discount_percent": forms.NumberInput(
                attrs={"class": "form-control", "step": "0.01", "min": "0"}
            ),
            "stock_quantity": forms.NumberInput(attrs={"class": "form-control", "min": "0"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "image_file": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-select"}),
            "manufacturer": forms.Select(attrs={"class": "form-select"}),
            "supplier": forms.Select(attrs={"class": "form-select"}),
        }
        labels = {
            "article": "Артикул",
            "name": "Наименование",
            "unit": "Ед. изм.",
            "price": "Цена, ₽",
            "discount_percent": "Скидка, %",
            "stock_quantity": "Кол-во на складе",
            "description": "Описание",
            "image_file": "Фото товара",
            "category": "Категория",
            "manufacturer": "Производитель",
            "supplier": "Поставщик",
        }


class OrderForm(forms.ModelForm):
    order_date = forms.DateField(
        label="Дата заказа",
        widget=forms.DateInput(
            attrs={"class": "form-control", "type": "date"},
            format="%Y-%m-%d",
        ),
        input_formats=["%Y-%m-%d"],
    )
    pickup_date = forms.DateField(
        label="Дата выдачи",
        required=False,
        widget=forms.DateInput(
            attrs={"class": "form-control", "type": "date"},
            format="%Y-%m-%d",
        ),
        input_formats=["%Y-%m-%d"],
    )

    class Meta:
        model = Order
        fields = [
            "order_number",
            "order_date",
            "pickup_date",
            "client_full_name",
            "pickup_code",
            "status",
            "pickup_point",
        ]
        widgets = {
            "order_number": forms.TextInput(
                attrs={"class": "form-control", "readonly": True}
            ),
            "client_full_name": forms.TextInput(attrs={"class": "form-control"}),
            "pickup_code": forms.TextInput(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "pickup_point": forms.Select(attrs={"class": "form-select"}),
        }
        labels = {
            "order_number": "Номер заказа",
            "client_full_name": "ФИО клиента",
            "pickup_code": "Код получения",
            "status": "Статус",
            "pickup_point": "Пункт выдачи",
        }
