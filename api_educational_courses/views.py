from rest_framework import permissions, filters
from .models import Course, UserProfile, Lesson, Enrollment, Review, Category
from .serializers import CourseModelSerializer, UserProfileModelSerializer, LessonModelSerializer, EnrollmentModelSerializer
from .serializers import ReviewModelSerializer, CategoryModelSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet


class CustomPermission(permissions.BasePermission):
    """
    Пользователи могут выполнять различные действия в зависимости от их роли.
    """

    def has_permission(self, request, view):
        """
        Метод для определения авторизации пользователя
        :param request: запрос
        :param view: представление
        :return: bool
        """

        # Разрешаем только GET запросы для не аутентифицированных пользователей
        if request.method == 'GET' and not request.user.is_authenticated:
            return True

        # Разрешаем GET и POST запросы для аутентифицированных пользователей
        if request.method in ['GET', 'POST'] and request.user.is_authenticated:
            return True

        # Разрешаем все действия для администраторов
        if request.user.is_superuser:
            return True

        # Во всех остальных случаях возвращаем False
        return False


class CustomPagination(PageNumberPagination):
    """
    Класс для кастомной пагинации
    """

    page_size = 3  # количество объектов на странице
    page_size_query_param = 'page_size'  # параметр запроса для настройки количества объектов на странице
    max_page_size = 1000  # максимальное количество объектов на странице


class CourseViewSet(ModelViewSet):
    """
    Класс для обработки данных, переданных пользователем,
    и взаимодействия с объектом модели базы данных Course
    """

    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'options']
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'name', 'description', 'author']
    search_fields = ['id', 'name', 'description', 'author']  # Поля, по которым будет выполняться поиск
    ordering_fields = ['id']  # Поля, по которым можно сортироват

    def get_permissions(self):
        """
        Метод для определения авторизации пользователя
        """

        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]  # Только админ может создавать, изменять, удалять
        return [permissions.AllowAny()]  # Пользователь может только смотреть


class UserProfileViewSet(ModelViewSet):
    """
    Класс для обработки данных, переданных пользователем,
    и взаимодействия с объектом модели базы данных UserProfile
    """

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileModelSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'options']
    permission_classes = [CustomPermission]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'name', 'teacher', 'user']
    search_fields = ['id', 'name', 'teacher', 'user']  # Поля, по которым будет выполняться поиск
    ordering_fields = ['id']  # Поля, по которым можно сортировать


class LessonViewSet(ModelViewSet):
    """
    Класс для обработки данных, переданных пользователем,
    и взаимодействия с объектом модели базы данных Lesson
    """

    queryset = Lesson.objects.all()
    serializer_class = LessonModelSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'options']
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'name', 'text', 'lesson_recording_url']
    search_fields = ['id', 'name', 'text', 'lesson_recording_url']  # Поля, по которым будет выполняться поиск
    ordering_fields = ['id']  # Поля, по которым можно сортировать

    def get_permissions(self):
        """
        Метод для определения авторизации пользователя
        """

        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]  # Только админ может создавать, изменять, удалять
        return [permissions.AllowAny()]  # Пользователь может только смотреть

class EnrollmentViewSet(ModelViewSet):
    """
    Класс для обработки данных, переданных пользователем,
    и взаимодействия с объектом модели базы данных Enrollment
    """

    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentModelSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'options']
    permission_classes = [CustomPermission]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'course', 'user']
    search_fields = ['id', 'course', 'user']  # Поля, по которым будет выполняться поиск
    ordering_fields = ['id']  # Поля, по которым можно сортировать


class ReviewViewSet(ModelViewSet):
    """
    Класс для обработки данных, переданных пользователем,
    и взаимодействия с объектом модели базы данных Review
    """

    queryset = Review.objects.all()
    serializer_class = ReviewModelSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'options']
    permission_classes = [CustomPermission]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'course', 'user', 'text', 'rate']
    search_fields = ['id', 'course', 'user', 'text', 'rate']  # Поля, по которым будет выполняться поиск
    ordering_fields = ['id']  # Поля, по которым можно сортировать


class CategoryViewSet(ModelViewSet):
    """
    Класс для обработки данных, переданных пользователем,
    и взаимодействия с объектом модели базы данных Category
    """

    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'options']
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'course', 'name']
    search_fields = ['id', 'course', 'name']  # Поля, по которым будет выполняться поиск
    ordering_fields = ['id']  # Поля, по которым можно сортировать

    def get_permissions(self):
        """
        Метод для определения авторизации пользователя
        """

        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]  # Только админ может создавать, изменять, удалять
        return [permissions.AllowAny()]  # Пользователь может только смотреть
