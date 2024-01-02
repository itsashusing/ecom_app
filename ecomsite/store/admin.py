from django.contrib import admin
from .models import Category, Product

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ['category_name', 'slug','id']


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ['product_name','id', 'slug','stock','created_date','is_available']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product,ProductAdmin)
