from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeacherViewSet, ClassPackViewSet, InstrumentViewSet, PriceViewSet, ClasseViewSet, LevelsViewSet, TeacherClasseViewSet, StudentViewSet, EnrollmentViewSet, ClassPackDiscountRulesViewSet, ClassPackClasseViewSet

router = DefaultRouter()
router.register(r'teachers', TeacherViewSet)
router.register(r'class_packs', ClassPackViewSet)
router.register(r'instruments', InstrumentViewSet)
router.register(r'prices', PriceViewSet)
router.register(r'classes', ClasseViewSet)
router.register(r'levels', LevelsViewSet)
router.register(r'teacher_classes', TeacherClasseViewSet)
router.register(r'students', StudentViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'class_pack_discount_rules', ClassPackDiscountRulesViewSet)
router.register(r'class_pack_classes', ClassPackClasseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
