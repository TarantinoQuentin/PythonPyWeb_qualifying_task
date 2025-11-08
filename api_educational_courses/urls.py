from django.urls import path, include
from .views import CourseViewSet, UserProfileViewSet, LessonViewSet, EnrollmentViewSet, ReviewViewSet, CategoryViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter


# app_name = 'api_educational_courses'

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')
router.register(r'user_profiles', UserProfileViewSet, basename='user-profiles')
router.register(r'lessons', LessonViewSet, basename='lessons')
router.register(r'enrollments', EnrollmentViewSet, basename='enrollments')
router.register(r'reviews', ReviewViewSet, basename='reviews')
router.register(r'categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Получение токена
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Обновление токена
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # Проверка токена
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('', include(router.urls)),
]
