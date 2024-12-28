from django.conf import settings
from django.db import models

from config.settings import AUTH_USER_MODEL


class Course(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название курса",
        help_text="введите название курса",
    )
    preview = models.ImageField(
        upload_to="materials/preview/course",
        verbose_name="Превью",
        blank=True,
        null=True,
    )
    description = models.TextField(
        verbose_name="Описание курса", help_text="укажите описание курса"
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Владелец",
        help_text="Укажите владельца курса",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(
        max_length=50, verbose_name="Название урока", help_text="укажите название урока"
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Курс",
        blank=True,
        null=True,
        related_name="lessons",
    )
    description = models.TextField(
        verbose_name="Описание урока", help_text="укажите описание урока"
    )
    preview = models.ImageField(
        upload_to="materials/preview/lesson",
        verbose_name="Картинка",
        blank=True,
        null=True,
    )
    link_to_video = models.CharField(
        max_length=200,
        verbose_name="Ссылка на видео",
        blank=True,
        null=True,
        help_text="укажите ссылку на видео материал",
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Владелец",
        help_text="Укажите владельца урока",
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.title
