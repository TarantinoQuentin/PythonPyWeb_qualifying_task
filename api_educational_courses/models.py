from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from datetime import date, datetime
from django.core import validators
"""
Рассматриваются 7 таблиц условно обобщающих функционал онлайн-курсов
"""

class User(AbstractUser):
    """
    Таблица 'Пользователь', содержащая в себе
    данные для авторизации
    """
    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"


class UserProfile(models.Model):
    """
    Таблица 'Профиль пользователя', содержащая в себе
    name - ФИО студента
    teacher - ФИО преподавателя
    user - связь с таблицей 'Пользователь'
    """

    name = models.CharField(max_length=40,
                            verbose_name="ФИО студента")
    teacher = models.CharField(max_length=40,
                               verbose_name="ФИО преподавателя")
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name="user_profile")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"



class Course(models.Model):
    """
    Таблица 'Курс', содержащая в себе
    name - название курса
    description - описание курса
    author - автор курса
    """

    name = models.CharField(max_length=30,
                            unique=True,
                            verbose_name="Название курса",
                            help_text="Название курса уникальное. Ограничение 30 знаков")
    description = models.CharField(max_length=150,
                                   null=True,
                                  blank=True,
                                  verbose_name="Описание курса",
                                  help_text="Направление курса? Для кого подойдет?")
    author = models.CharField(max_length=40,
                              verbose_name="Автор курса")

    def __str__(self):
        return f'{self.name}, автор: {self.author}'

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    """
    Таблица 'Урок', содержащая в себе
    name - название урока
    text - описание урока
    lesson_recording_url - ссылка на запись урока
    """

    name = models.CharField(max_length=20,
                            unique=True,
                            verbose_name="Название урока",
                            help_text="Название урока уникальное. Ограничение 20 знаков")
    text = models.TextField(blank=False,
                            null=False,
                            help_text="Содержание лекции")
    lesson_recording_url = models.URLField(max_length=200,
                                           verbose_name="Ссылка на запись урока")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Enrollment(models.Model):
    """
    Таблица 'Запись на курс', содержащая в себе
    user - связь с конкретным пользователем, записанным на курсы
    course - курс обучения
    """
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="enrollments",
                             verbose_name="Пользователь")
    course = models.ManyToManyField('Course', related_name='enrollments')

    def __str__(self):
        # course_list = []
        # for value in self.course:
        #     self.course.name.append(course_list)
        return f'{",,,".join([course.name for course in self.course.all()])}, студент: {self.user}'

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"


class Review(models.Model):
    """
    Таблица 'Отзывы', содержащая в себе
    course - связь с конкретным курсом обучения
    user - связь с конкретным пользователем, автором отзыва
    text - текст отзыва
    rate - оценка
    """

    course = models.ForeignKey(Course,
                               on_delete=models.CASCADE,
                               related_name='reviews')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='reviews')
    text = models.TextField(blank=True,
                            null=True,
                            help_text="Текст отзыва")
    rate = models.IntegerField(null=False,
                               blank=False,
                             default=0,
                             verbose_name="Оценка",
                             help_text="От 1 до 10",
                               validators=[validators.MinValueValidator(0), validators.MaxValueValidator(10)],
                               error_messages={'blank': 'ПУстые данные', 'required': 'Обязательное поле', 'null':'null', 'invalid':'invalid'})


    def __str__(self):
        return f'({self.rate:.0f}/10) {self.course}, студент: {self.user}'

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class Category(models.Model):
    """
    Таблица 'Категории', содержащая в себе
    name - название категории
    course - курсы категории
    """

    name = models.CharField(max_length=30,
                            unique=True,
                            verbose_name="Название категории",
                            help_text="Название категории уникальное. Ограничение 15 знаков")
    course = models.ManyToManyField('Course', related_name='categories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
