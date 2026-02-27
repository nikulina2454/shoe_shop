import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from decimal import Decimal
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True, verbose_name="Категория")),
            ],
            options={"ordering": ["name"]},
        ),
        migrations.CreateModel(
            name="Manufacturer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=100, unique=True, verbose_name="Производитель"),
                ),
            ],
            options={"ordering": ["name"]},
        ),
        migrations.CreateModel(
            name="Supplier",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True, verbose_name="Поставщик")),
            ],
            options={"ordering": ["name"]},
        ),
        migrations.CreateModel(
            name="Unit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=100, unique=True, verbose_name="Единица измерения"),
                ),
            ],
            options={"ordering": ["name"]},
        ),
        migrations.CreateModel(
            name="PickupPoint",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        max_length=500, unique=True, verbose_name="Адрес пункта выдачи"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Role",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("client", "Авторизованный клиент"),
                            ("manager", "Менеджер"),
                            ("admin", "Администратор"),
                        ],
                        max_length=25,
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("last_login", models.DateTimeField(blank=True, null=True, verbose_name="last login")),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={"unique": "A user with that username already exists."},
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                        verbose_name="username",
                    ),
                ),
                ("first_name", models.CharField(blank=True, max_length=150, verbose_name="first name")),
                ("last_name", models.CharField(blank=True, max_length=150, verbose_name="last name")),
                ("email", models.EmailField(blank=True, max_length=254, verbose_name="email address")),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(default=django.utils.timezone.now, verbose_name="date joined"),
                ),
                ("full_name", models.CharField(blank=True, max_length=255, verbose_name="ФИО")),
                ("login", models.CharField(blank=True, max_length=150, unique=True, verbose_name="Логин")),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
                (
                    "role",
                    models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to="body.role"),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[("objects", django.contrib.auth.models.UserManager())],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("article", models.CharField(max_length=50, unique=True, verbose_name="Артикул")),
                ("name", models.CharField(max_length=255, verbose_name="Наименование")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        validators=[django.core.validators.MinValueValidator(Decimal("0.00"))],
                        verbose_name="Цена",
                    ),
                ),
                (
                    "discount_percent",
                    models.DecimalField(
                        decimal_places=2,
                        default=Decimal("0.00"),
                        max_digits=5,
                        validators=[django.core.validators.MinValueValidator(Decimal("0.00"))],
                        verbose_name="Скидка %",
                    ),
                ),
                (
                    "stock_quantity",
                    models.IntegerField(
                        default=0,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="Кол-во на складе",
                    ),
                ),
                ("description", models.TextField(blank=True, verbose_name="Описание")),
                ("image_file", models.ImageField(blank=True, null=True, upload_to="products/", verbose_name="Фото")),
                ("category", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="body.category")),
                (
                    "manufacturer",
                    models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="body.manufacturer"),
                ),
                ("supplier", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="body.supplier")),
                ("unit", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="body.unit", verbose_name="Ед. изм.")),
            ],
            options={"ordering": ["name"]},
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order_number", models.CharField(max_length=50, unique=True, verbose_name="Номер заказа")),
                ("order_date", models.DateField(blank=True, null=True, verbose_name="Дата заказа")),
                ("pickup_date", models.DateField(blank=True, null=True, verbose_name="Дата выдачи")),
                ("client_full_name", models.CharField(max_length=255, verbose_name="ФИО клиента")),
                ("pickup_code", models.CharField(blank=True, max_length=20, null=True, verbose_name="Код получения")),
                (
                    "status",
                    models.CharField(
                        choices=[("new", "Новый"), ("completed", "Завершён"), ("cancelled", "Отменён")],
                        default="new",
                        max_length=20,
                        verbose_name="Статус",
                    ),
                ),
                ("pickup_point", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="body.pickuppoint")),
            ],
            options={"ordering": ["-order_date"]},
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "quantity",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(1)],
                        verbose_name="Количество",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="body.order",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="body.product"),
                ),
            ],
        ),
    ]
