from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny


from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer
from rest_framework.response import Response
from materials.models import Course
from users.services import (
    create_stripe_checkout_sessions,
    create_stripe_product,
    create_stripe_price,
)

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["course", "lesson", "payment_method"]
    ordering_fields = ["payment_date"]


class PaymentCreateAPIView(CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save()
        if payment.course:
            product_name = f"{payment.course.title} Course"
        else:
            product_name = "General Course"
        product = create_stripe_product(product_name)
        price = create_stripe_price(payment.amount, product)

        # Создание сессии для оплаты
        session_id, payment_link = create_stripe_checkout_sessions(price)

        # Сохранение данных в модель Payments
        payment.stripe_session_id = session_id
        payment.link = payment_link
        payment.save()


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
