from django.db import models
from django.shortcuts import reverse

class Product(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    info = models.TextField(blank=True, db_index=True)
    price = models.IntegerField(default=0)
    cats = models.ManyToManyField("Category", blank=True, related_name="products")
    image = models.ImageField(upload_to="images/", default="images/default.jpg")

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("product_detail_url", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["-price"]

class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("category_detail_url", kwargs={"pk": self.pk})   

class Order(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name