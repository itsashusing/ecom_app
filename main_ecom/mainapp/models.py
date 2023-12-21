from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
CATEGORY_CHOICES = (
    ('S', 'Shirt'),
    ('SW', 'Sport Wear'),
    ('OW', 'Outwear')
)
LABEL_CHOICES = (
    ('P', 'primary'),
    ('W', 'warning'),
    ('D', 'danger')
)


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(null=True, blank=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    slug = models.SlugField()
    discription = models.TextField()

    def get_absolute_url(self):
        return reverse("main_ecom: home", kwargs={
            'slug': self.slug
        })

    def __str__(self):
        return f'{self.title}'


class OrderItem(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.item} of | {self.user} |'

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_total_save(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        else:
            return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True)
    order_date = models.DateTimeField()

    def get_total_sum(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total
    

    def __str__(self):
        return f'{self.user} '
