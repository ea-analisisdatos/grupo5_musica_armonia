from rest_framework import viewsets
from .models import Teacher, ClassPack, Instrument, Price, Classe, Level, TeacherClasse, Student, Enrollment, ClassPackDiscountRules, ClassPackClasse
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

class ClasseViewSet(viewsets.ModelViewSet):
    queryset = Classe.objects.all()
    serializer_class = ClassesSerializer

class LevelsViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelsSerializer

class TeacherClasseViewSet(viewsets.ModelViewSet):
    queryset = TeacherClasse.objects.all()
    serializer_class = TeacherClassesSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentsSerializer

class ClassPackDiscountRulesViewSet(viewsets.ModelViewSet):
    queryset = ClassPackDiscountRules.objects.all()
    serializer_class = ClassPackDiscountRulesSerializer

class ClassPackClasseViewSet(viewsets.ModelViewSet):
    queryset = ClassPackClasse.objects.all()
    serializer_class = ClassPackClassesSerializer
