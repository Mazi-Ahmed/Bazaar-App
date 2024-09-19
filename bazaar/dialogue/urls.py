from django import path
from .import views

app_name = 'dialogue'

urlpatterns = [
    path('new/<int:product_pk>/', views.new_dialogue, name='new'),
]