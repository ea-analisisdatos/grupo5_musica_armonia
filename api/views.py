from rest_framework import viewsets
from .models import Teacher, ClassPack, Instrument, Price, Classes, Levels, TeacherClasses, Students, Enrollments, ClassPackDiscountRules, ClassPackClasses
from .serializers import TeacherSerializer, ClassPackSerializer, InstrumentSerializer, PriceSerializer, ClassesSerializer, LevelsSerializer, TeacherClassesSerializer, StudentsSerializer, EnrollmentsSerializer, ClassPackDiscountRulesSerializer, ClassPackClassesSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class ClassPackViewSet(viewsets.ModelViewSet):
    queryset = ClassPack.objects.all()
    serializer_class = ClassPackSerializer

class InstrumentViewSet(viewsets.ModelViewSet):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer

class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

class ClassesViewSet(viewsets.ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer

class LevelsViewSet(viewsets.ModelViewSet):
    queryset = Levels.objects.all()
    serializer_class = LevelsSerializer

class TeacherClassesViewSet(viewsets.ModelViewSet):
    queryset = TeacherClasses.objects.all()
    serializer_class = TeacherClassesSerializer

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

class EnrollmentsViewSet(viewsets.ModelViewSet):
    queryset = Enrollments.objects.all()
    serializer_class = EnrollmentsSerializer

class ClassPackDiscountRulesViewSet(viewsets.ModelViewSet):
    queryset = ClassPackDiscountRules.objects.all()
    serializer_class = ClassPackDiscountRulesSerializer

class ClassPackClassesViewSet(viewsets.ModelViewSet):
    queryset = ClassPackClasses.objects.all()
    serializer_class = ClassPackClassesSerializer
