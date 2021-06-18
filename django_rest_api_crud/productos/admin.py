from django.contrib import admin

from .models import CategoriaProd,Producto


class CategoriaProdAdmin(admin.ModelAdmin):
    list_display = ("nombre", "created", "updated")
    readonly_fields = ("created", "updated")

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre","precio","disponibilidad", "created", "updated")
    readonly_fields = ("created", "updated")


admin.site.register(CategoriaProd, CategoriaProdAdmin)
admin.site.register(Producto, ProductoAdmin)