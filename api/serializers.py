from rest_framework import serializers
from .models import Teacher, ClassPack, Instrument, Price, Classe, Level, TeacherClasse, Student, Enrollment, ClassPackDiscountRules, ClassPackClasse

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class ClassPackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPack
        fields = '__all__'

class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = '__all__'

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'

class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = '__all__'

class LevelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'

class TeacherClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherClasse
        fields = '__all__'

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class EnrollmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'

class ClassPackDiscountRulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPackDiscountRules
        fields = '__all__'

class ClassPackClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPackClasse
        fields = '__all__'
