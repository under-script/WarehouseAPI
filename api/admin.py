from django.contrib import admin

from api.models import Product, Material, ProductMaterial, Warehouse


class BaseAdmin(admin.ModelAdmin):
    list_per_page = 10

    class Meta:
        abstract = True

class ProductAdmin(BaseAdmin):
    list_display = [f.name for f in Product._meta.fields]

class MaterialAdmin(BaseAdmin):
    list_display = [f.name for f in Material._meta.fields]

class ProductMaterialAdmin(BaseAdmin):
    list_display = [f.name for f in ProductMaterial._meta.fields]

class WarehouseAdmin(BaseAdmin):
    list_display = [f.name for f in Warehouse._meta.fields]


admin.site.register(Product, ProductAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(ProductMaterial, ProductMaterialAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
