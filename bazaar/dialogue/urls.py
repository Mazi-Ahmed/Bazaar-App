from django.urls import path
from .import views

app_name = 'dialogue'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('<int:pk>/', views.detail, name='detail'),
    path('new/<int:product_pk>/', views.new_dialogue, name='new'),
]