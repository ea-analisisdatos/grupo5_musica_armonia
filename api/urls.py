from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeacherViewSet, ClassPackViewSet, InstrumentViewSet, PriceViewSet, ClassViewSet, LevelViewSet, TeacherClassViewSet, StudentViewSet, EnrollmentViewSet, ClassPackDiscountRuleViewSet, ClassPackClassViewSet, home
from . import views

router = DefaultRouter()
router.register(r'teacher', TeacherViewSet)
router.register(r'class_pack', ClassPackViewSet)
router.register(r'instrument', InstrumentViewSet)
router.register(r'price', PriceViewSet)
router.register(r'class', ClassViewSet)
router.register(r'level', LevelViewSet)
router.register(r'teacher_class', TeacherClassViewSet)
router.register(r'student', StudentViewSet)
router.register(r'enrollment', EnrollmentViewSet)
router.register(r'class_pack_discount_rule', ClassPackDiscountRuleViewSet)
router.register(r'class_pack_class', ClassPackClassViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', home, name='home'),
    path('create-enrollment/', views.create_enrollment, name='create_enrollment'),
    path('create-student/', views.create_student, name='create_student'),
    path('create_teacher/', views.create_teacher, name='create_teacher'),
    path('execute_query/', views.execute_query, name='execute_query'),
    path('create_instrument/', views.create_instrument, name='create_instrument'),
    path('delete_teacher/<int:teacher_id>/', views.delete_teacher, name='confirm_delete_teacher'),
    path('edit_teacher/<int:teacher_id>/', views.edit_teacher, name='edit_teacher'),
    path('create_class_pack/', views.create_class_pack, name='create_class_pack'),
    path('edit_class_pack/<int:pk>/', views.edit_class_pack, name='edit_class_pack'),
    path('delete_class_pack/<int:pk>/', views.delete_class_pack, name='confirm_delete_class_pack'),
    path('edit_price/<int:pk>/', views.edit_price, name='edit_price'),
]