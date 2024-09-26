from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    icon_class = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
        
class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images', blank=True, null=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    item_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE) 
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name