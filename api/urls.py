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
    path('execute_query_month/', views.execute_query_month, name='execute_query_month'),
    path('execute_query_total_due/', views.execute_query_total_due, name='execute_query_total_due'),
    path('create_instrument/', views.create_instrument, name='create_instrument'),
    path('delete_teacher/<int:teacher_id>/', views.delete_teacher, name='confirm_delete_teacher'),
    path('edit_teacher/<int:teacher_id>/', views.edit_teacher, name='edit_teacher'),
    path('create_class_pack/', views.create_class_pack, name='create_class_pack'),
    path('edit_class_pack/<int:pk>/', views.edit_class_pack, name='edit_class_pack'),
    path('delete_class_pack/<int:pk>/', views.delete_class_pack, name='confirm_delete_class_pack'),
    path('edit_price/<int:pk>/', views.edit_price, name='edit_price'),
    path('delete_instrument/<int:instrument_id>/', views.delete_instrument, name='delete_instrument'),
    path('edit_instrument/<int:instrument_id>/', views.edit_instrument, name='edit_instrument'),  
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('edit_student/<int:student_id>/', views.edit_student, name='edit_student'),  

]