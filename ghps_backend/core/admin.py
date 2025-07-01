from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Farm, Product, Order, OrderItem, LearningMaterial, AIQuestion

# User admin
class UserAdmin(BaseUserAdmin):
    def is_farmer(self, obj):
        return obj.role == 'farmer'
    is_farmer.boolean = True
    is_farmer.short_description = 'Is Farmer'

    list_display = ('username', 'email', 'is_farmer', 'is_staff')
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )

admin.site.register(User, UserAdmin)

# Farm admin
@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'location', 'created_at')
    search_fields = ('name', 'location')
    list_filter = ('created_at',)

# Product admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'farm', 'category', 'price', 'stock', 'created_at')
    search_fields = ('name', 'category')
    list_filter = ('category',)

# Order admin
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'farm', 'status', 'total', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username',)

# OrderItem admin
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')

# LearningMaterial admin
@admin.register(LearningMaterial)
class LearningMaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'stage', 'created_at')
    search_fields = ('title',)
    list_filter = ('stage',)

# AIQuestion admin
@admin.register(AIQuestion)
class AIQuestionAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'created_at')
    search_fields = ('question',)
