from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(unique=True, max_length=15)
    address = models.TextField()
    date_birth = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name_product = models.CharField(unique=True, max_length=100)
    description_product = models.TextField()
    price_product = models.DecimalField(max_digits=10, decimal_places=2)
    number_product = models.PositiveIntegerField()
    date_addition = models.DateTimeField(auto_now_add=True)
    img_product = models.ImageField(upload_to='products/', null=True)

    def __str__(self):
        return self.name_product


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    general_sum = models.DecimalField(max_digits=10, decimal_places=2)
    formation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Заказ #{self.id} от {self.formation_date};"
