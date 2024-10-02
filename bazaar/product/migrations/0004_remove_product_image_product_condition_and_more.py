# Generated by Django 4.2.16 on 2024-10-01 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_category_icon_class'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='condition',
            field=models.CharField(blank=True, choices=[('new', 'New'), ('used_like_new', 'Used - Like New'), ('used_good', 'Used - Good'), ('used_acceptable', 'Used - Acceptable')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.product')),
            ],
        ),
    ]
