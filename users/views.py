from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["course", "lesson", "payment_method"]
    ordering_fields = ["payment_date"]


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
