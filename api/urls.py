from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeacherViewSet, ClassPackViewSet, InstrumentViewSet, PriceViewSet, ClassesViewSet, LevelsViewSet, TeacherClassesViewSet, StudentsViewSet, EnrollmentsViewSet, ClassPackDiscountRulesViewSet, ClassPackClassesViewSet

router = DefaultRouter()
router.register(r'teachers', TeacherViewSet)
router.register(r'class_packs', ClassPackViewSet)
router.register(r'instruments', InstrumentViewSet)
router.register(r'prices', PriceViewSet)
router.register(r'classes', ClassesViewSet)
router.register(r'levels', LevelsViewSet)
router.register(r'teacher_classes', TeacherClassesViewSet)
router.register(r'students', StudentsViewSet)
router.register(r'enrollments', EnrollmentsViewSet)
router.register(r'class_pack_discount_rules', ClassPackDiscountRulesViewSet)
router.register(r'class_pack_classes', ClassPackClassesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
