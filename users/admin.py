from django.contrib import admin

from users.models import Payment, User
from django.contrib import admin
from materials.models import Subscription


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ("id", "email", "groups")


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("user", "amount", "payment_date")


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('owner', 'course')
