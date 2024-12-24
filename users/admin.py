from django.contrib import admin
from .models import Payment, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ("id", "email")

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'payment_date')








