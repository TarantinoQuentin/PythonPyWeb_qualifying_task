from rest_framework import serializers
from api_educational_courses.models import Course


class CourseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = 'id'
