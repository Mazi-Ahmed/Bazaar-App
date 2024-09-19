from django.db import models
from django.contrib.auth.models import User
from product.models import Product

class Dialogue(models.Model):
    product = models.ForeignKey(Product, related_name='dialogues', on_delete=models.CASCADE)
    messengers = models.ManyToManyField(User, related_name='dialogues')
    date_of = models.DateTimeField(auto_now_add=True)
    status = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-status',)

class DialogueText(models.Model):
    dialogue = models.ForeignKey(Dialogue, related_name='dm_messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_of = models.DateTimeField(auto_now_add=True)
    created_dialogue = models.ForeignKey(User, related_name='created_dm', on_delete=models.CASCADE)