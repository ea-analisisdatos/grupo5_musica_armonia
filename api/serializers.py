from rest_framework import serializers
from .models import Teacher, ClassPack, Instrument, Price, Classes, Levels, TeacherClasses, Students, Enrollments, ClassPackDiscountRules, ClassPackClasses

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
        model = Classes
        fields = '__all__'

class LevelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Levels
        fields = '__all__'

class TeacherClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherClasses
        fields = '__all__'

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

class EnrollmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollments
        fields = '__all__'

class ClassPackDiscountRulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPackDiscountRules
        fields = '__all__'

class ClassPackClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPackClasses
        fields = '__all__'
