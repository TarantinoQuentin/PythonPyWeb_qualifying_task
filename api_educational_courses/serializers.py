from rest_framework import serializers
from api_educational_courses.models import Course, UserProfile, Lesson, Enrollment, Review, Category
from django.core import validators


class CourseModelSerializer(serializers.ModelSerializer):
    """
    Удалить, создать, обновить и вернуть новый объект Course на основе предоставленных данных
    """

    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ['id']


class UserProfileModelSerializer(serializers.ModelSerializer):
    """
    Удалить, создать, обновить и вернуть новый объект UserProfile на основе предоставленных данных
    """

    class Meta:
        model = UserProfile
        fields = '__all__'
        read_only_fields = ['id']


class LessonModelSerializer(serializers.ModelSerializer):
    """
    Удалить, создать, обновить и вернуть новый объект Lesson на основе предоставленных данных
    """

    class Meta:
        model = Lesson
        fields = '__all__'
        read_only_fields = ['id']


class EnrollmentModelSerializer(serializers.ModelSerializer):
    """
    Удалить, создать, обновить и вернуть новый объект Enrollment на основе предоставленных данных
    """

    class Meta:
        model = Enrollment
        fields = '__all__'
        read_only_fields = ['id']


class ReviewModelSerializer(serializers.ModelSerializer):
    """
    Удалить, создать, обновить и вернуть новый объект Review на основе предоставленных данных
    """

    rate = serializers.IntegerField(validators=[validators.MinValueValidator(0), validators.MaxValueValidator(10)])

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['id']


class CategoryModelSerializer(serializers.ModelSerializer):
    """
    Удалить, создать, обновить и вернуть новый объект Category на основе предоставленных данных
    """

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['id']
