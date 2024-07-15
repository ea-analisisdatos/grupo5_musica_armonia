# api/views.py

from rest_framework import viewsets
from .models import Teacher, ClassPack, Instrument, Price, Class, Level, TeacherClass, Student, Enrollment, ClassPackDiscountRule, ClassPackClass
from .serializers import TeacherSerializer, ClassPackSerializer, InstrumentSerializer, PriceSerializer, ClassSerializer, LevelSerializer, TeacherClassSerializer, StudentSerializer, EnrollmentSerializer, ClassPackDiscountRuleSerializer, ClassPackClassSerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import EnrollmentForm, StudentForm, TeacherForm, InstrumentForm, ClassPackForm, PriceForm
from django import forms
from django.db import connection

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

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class TeacherClassViewSet(viewsets.ModelViewSet):
    queryset = TeacherClass.objects.all()
    serializer_class = TeacherClassSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class ClassPackDiscountRuleViewSet(viewsets.ModelViewSet):
    queryset = ClassPackDiscountRule.objects.all()
    serializer_class = ClassPackDiscountRuleSerializer

class ClassPackClassViewSet(viewsets.ModelViewSet):
    queryset = ClassPackClass.objects.all()
    serializer_class = ClassPackClassSerializer

def home(request):
    context = {
        'teachers': Teacher.objects.all(),
        'class_packs': ClassPack.objects.all(),
        'instruments': Instrument.objects.all(),
        'prices': Price.objects.all(),
        'classes': Class.objects.all(),
        'levels': Level.objects.all(),
        'teacher_classes': TeacherClass.objects.all(),
        'students': Student.objects.all(),
        'enrollments': Enrollment.objects.all(),
        'class_pack_discounts': ClassPackDiscountRule.objects.all(),
        'class_pack_classes': ClassPackClass.objects.all(),
    }
    return render(request, 'api/home.html', context)

def create_enrollment(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EnrollmentForm()

    context = {
        'form': form,
    }
    return render(request, 'api/create_enrollment.html', context)

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()

    context = {
        'form': form,
    }
    return render(request, 'api/create_student.html', context)

def create_instrument(request):
    if request.method == 'POST':
        form = InstrumentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = InstrumentForm()

    context = {
        'form': form,
    }
    return render(request, 'api/create_instrument.html', context)

def create_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TeacherForm()

    context = {
        'form': form,
    }
    return render(request, 'api/create_teacher.html', context)

def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    if request.method == 'POST':
        teacher.delete()
        return redirect('home')  # Ajusta 'home' según el nombre de tu vista principal
    context = {
    'object_type': 'profesor',  # Especifica aquí el tipo de objeto que estás eliminando
    'teacher': teacher
    }
    return render(request, 'api/confirm_delete.html', context)

def delete_instrument(request, instrument_id):
    instrument = get_object_or_404(Instrument, id=instrument_id)
    if request.method == 'POST':
        instrument.delete()
        return redirect('home')  # Ajusta 'home' según el nombre de tu vista principal
    context = {
        'object_type': 'instrumento',  # Especifica aquí el tipo de objeto que estás eliminando
        'teacher': instrument
    }
    return render(request, 'api/confirm_delete.html', context)

def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('home')  # Ajusta 'home' según el nombre de tu vista principal
    context = {
        'object_type': 'alumno',  # Especifica aquí el tipo de objeto que estás eliminando
        'teacher': student
    }
    return render(request, 'api/confirm_delete.html', context)

def edit_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'api/edit_teacher.html', {'form': form})


def create_class_pack(request):
    if request.method == 'POST':
        form = ClassPackForm(request.POST)
        form = ClassPackForm()
    return render(request, 'api/create_class_pack.html', {'form': form})

def edit_instrument(request, instrument_id):
    instrument = get_object_or_404(Instrument, id=instrument_id)
    if request.method == 'POST':
        form = InstrumentForm(request.POST, instance=instrument)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = InstrumentForm(instance=instrument)
    return render(request, 'api/edit_instrument.html', {'form': form})
        

def edit_class_pack(request, pk):
    class_pack = get_object_or_404(ClassPack, pk=pk)
    if request.method == 'POST':
        form = ClassPackForm(request.POST, instance=class_pack)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClassPackForm(instance=class_pack)
    return render(request, 'api/edit_class_pack.html', {'form': form})

def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm(instance=student)
    return render(request, 'api/edit_student.html', {'form': form})


def delete_class_pack(request, pk):
    class_pack = get_object_or_404(ClassPack, pk=pk)
    if request.method == 'POST':
        class_pack.delete()
        return redirect('home')
    context = {
    'object_type': 'paquete de clases',  # Especifica aquí el tipo de objeto que estás eliminando
    'class_pack': class_pack
    }
    return render(request, 'api/confirm_delete.html', context)

def edit_price(request, pk):
    price = get_object_or_404(Price, pk=pk)
    if request.method == 'POST':
        form = PriceForm(request.POST, instance=price)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PriceForm(instance=price)
    return render(request, 'api/edit_price.html', {'form': form, 'price': price})

def execute_query_month(request):
    with connection.cursor() as cursor:
        # Configurar el idioma español para la conexión
        cursor.execute("SET lc_time_names = 'es_ES';")
        
        # Ejecutar la consulta principal
        cursor.execute("""
            SELECT
                DATE_FORMAT(e.enrollment_date, '%m-%Y') AS `Mes de inscripción`,
                COUNT(*) AS `Total Inscripciones`,
                GROUP_CONCAT(DISTINCT CONCAT(s.first_name, ' ', s.last_name, ' (', sub.count_per_student, ')') ORDER BY s.last_name SEPARATOR ', ') AS `Estudiantes inscritos`
            FROM
                Enrollment e
            JOIN
                Student s ON e.student_id = s.id
            JOIN (
                SELECT student_id, DATE_FORMAT(enrollment_date, '%m-%Y') AS enrollment_month, COUNT(*) AS count_per_student
                FROM Enrollment
                GROUP BY student_id, DATE_FORMAT(enrollment_date, '%m-%Y')
            ) sub ON e.student_id = sub.student_id AND DATE_FORMAT(e.enrollment_date, '%m-%Y') = sub.enrollment_month
            GROUP BY
                DATE_FORMAT(e.enrollment_date, '%m-%Y')
            ORDER BY
                `mes de inscripción`;
        """)
        columns = [col[0] for col in cursor.description]
        data = cursor.fetchall()

    return render(request, 'api/query_results_month.html', {'columns': columns, 'data': data})

def execute_query_total_due(request):
    with connection.cursor() as cursor:
        # Ejecutar la nueva consulta
        cursor.execute("""
            SELECT 
                s.first_name AS Nombre,
                s.last_name AS Apellidos,
                CONCAT(FORMAT(
                    SUM(
                        CASE 
                            WHEN e.class_number = 1 THEN 
                                p.amount  -- Primera clase, sin descuento
                            WHEN e.class_number = 2 THEN 
                                p.amount * 0.5  -- Segunda clase, 50% descuento
                            WHEN e.class_number >= 3 THEN 
                                p.amount * 0.25  -- Tercera o más, 75% descuento
                            ELSE 
                                p.amount  -- Caso por defecto (sin descuento)
                        END * 
                        (CASE 
                            WHEN s.family_discount = TRUE THEN 0.9  -- Aplica un 10% de descuento adicional si hay descuento familiar
                            ELSE 1  -- Sin descuento adicional
                        END)
                    ), 2
                ), ' €') AS "Total Deuda"
            FROM 
                Student s
            JOIN 
                Enrollment e ON s.id = e.student_id
            JOIN 
                Class c ON e.class_id = c.id
            JOIN 
                Price p ON c.price_id = p.id
            GROUP BY 
                s.id, s.first_name, s.last_name
            ORDER BY 
                s.last_name, s.first_name;
        """)
        columns = [col[0] for col in cursor.description]
        data = cursor.fetchall()

    return render(request, 'api/query_results_total_due.html', {'columns': columns, 'data': data})

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = '__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
