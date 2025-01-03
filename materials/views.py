from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from materials.models import Course, Lesson, Subscription
from materials.paginations import CustomPagination

from materials.serializers import CourseSerializer, LessonSerializer
from users.permissions import IsModer, IsOwner


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_description="description from swagger_auto_schema via method_decorator"
    ),
)
class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get_serializer_context(self):
        """
        Метод для добавления текущего пользователя в контекст сериализатора
        """
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    def perform_create(self, serializer):
        """Привязка курса к авторизованному пользователю"""
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes.extend([~IsModer])
        elif self.action in ["update", "retrieve"]:
            self.permission_classes.extend([IsModer | IsOwner])
        elif self.action == "destroy":
            self.permission_classes.extend([~IsModer, IsOwner])
        return super().get_permissions()


class LessonListAPIView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModer | IsOwner]
    pagination_class = CustomPagination


class LessonCreateAPIView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        """Привязка урока к авторизованному пользователю"""
        serializer.save(owner=self.request.user)


#   def perform_create(self, serializer):
#       """Привязка урока к авторизованному пользователю"""
#       lesson = serializer.save()
#       lesson.owner = self.request.user
#       lesson.save()


class LessonRetrieveAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModer | IsOwner]


class LessonUpdateAPIView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsModer]


class LessonDestroyAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class SubscriptionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        course_id = request.data.get("course_id")
        course = get_object_or_404(Course, id=course_id)
        subs_item = Subscription.objects.filter(owner=request.user, course=course)

        if subs_item.exists():
            subs_item.delete()
            message = "Подписка удалена."
        else:
            Subscription.objects.create(owner=request.user, course=course)
            message = "Подписка добавлена."

        return Response({"message": message})
