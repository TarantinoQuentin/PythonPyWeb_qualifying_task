from django.contrib import admin
from .models import Course, User, UserProfile, Lesson, Enrollment, Review, Category
from django.apps import apps

app = apps.get_app_config('api_educational_courses')
app.verbose_name = 'Приложение "Онлайн школа курсов"'  # Чтобы изменить название при отображении в админ панели (другой вариант приведен в apps.py)

admin.site.register(Course)
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Lesson)
admin.site.register(Enrollment)
admin.site.register(Review)
admin.site.register(Category)
