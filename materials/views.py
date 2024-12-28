from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer
from users.permissions import IsModer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    #permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Привязка курса к авторизованному пользователю"""
        #serializer.save(owner=self.request.user)
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            self.permission_classes = (~IsModer,)
        elif self.action in ['update', 'retrieve']:
            self.permission_classes = (IsModer,)
        return super().get_permissions()



class LessonListAPIView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    #permission_classes = [IsAuthenticated, IsModer | IsOwner]

class LessonCreateAPIView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

   # def perform_create(self, serializer):
   #     """Привязка урока к авторизованному пользователю"""
   #     #serializer.save(owner=self.request.user)
   #     lesson = serializer.save()
   #     lesson.owner = self.request.user
  #      lesson.save()

class LessonRetrieveAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
   # permission_classes = [IsAuthenticated, IsModer | IsOwner]


class LessonUpdateAPIView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    #permission_classes = [IsAuthenticated, IsModer | IsOwner]


class LessonDestroyAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
   # permission_classes = [IsAuthenticated, IsOwner]

