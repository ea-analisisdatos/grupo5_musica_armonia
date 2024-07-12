import pytest
from django.test import TestCase
from api.models import Teacher, ClassPack, Instrument, Price, Classe, Level, TeacherClasse, Student, Enrollment, ClassPackDiscountRules, ClassPackClasse


@pytest.mark.django_db
class TestModels(TestCase):
    def test_teacher_model(self):
        teacher = Teacher.objects.create(name="John Doe")
        assert teacher.name == "John Doe"

    def test_classpack_model(self):
        class_pack = ClassPack.objects.create(name="Class Pack A")
        assert class_pack.name == "Class Pack A"

    def test_instrument_model(self):
        instrument = Instrument.objects.create(name="Piano")
        assert instrument.name == "Piano"

    def test_price_model(self):
        price = Price.objects.create(amount=100.00, description="Standard Price")
        assert str(price) == "100.0 - Standard Price"

    def test_Classe_model(self):
        instrument = Instrument.objects.create(name="Guitar")
        price = Price.objects.create(amount=80.00, description="Beginner Class Price")
        _class = Classe.objects.create(name="Guitar Beginner", instrument=instrument, price=price)
        assert _class.name == "Guitar Beginner"

    def test_level_model(self):
        instrument = Instrument.objects.create(name="Violin")
        price = Price.objects.create(amount=90.00, description="Intermediate Class Price")
        _class = Classe.objects.create(name="Violin Intermediate", instrument=instrument, price=price)
        level = Level.objects.create(name="Intermediate Level", _class=_class)
        assert str(level) == "Intermediate Level - Violin Intermediate"

    def test_teacherClasse_model(self):
        teacher = Teacher.objects.create(name="Jane Smith")
        instrument = Instrument.objects.create(name="Flute")
        price = Price.objects.create(amount=70.00, description="Advanced Class Price")
        _class = Classe.objects.create(name="Flute Advanced", instrument=instrument, price=price)
        teacher_class = TeacherClasse.objects.create(teacher=teacher, _class=_class)
        assert str(teacher_class) == "Jane Smith - Flute Advanced"

    def test_Student_model(self):
        student = Student.objects.create(first_name="Alice", last_name="Johnson", age=25)
        assert str(student) == "Alice Johnson"

    def test_Enrollment_model(self):
        student = Student.objects.create(first_name="Bob", last_name="Brown", age=30)
        instrument = Instrument.objects.create(name="Drums")
        price = Price.objects.create(amount=95.00, description="Advanced Class Price")
        _class = Classe.objects.create(name="Drums Advanced", instrument=instrument, price=price)
        enrollment = Enrollment.objects.create(student=student, _class=_class, enrollment_date="2024-07-10")
        assert str(enrollment) == "Bob Brown - Drums Advanced"

    def test_classpackdiscountrules_model(self):
        class_pack = ClassPack.objects.create(name="Class Pack B")
        discount_rule = ClassPackDiscountRules.objects.create(class_pack=class_pack, class_number=3, discount_percentage=10.00)
        assert str(discount_rule) == "Class Pack B - 3"

    def test_classpackClasse_model(self):
        class_pack = ClassPack.objects.create(name="Class Pack C")
        instrument = Instrument.objects.create(name="Trumpet")
        price = Price.objects.create(amount=85.00, description="Intermediate Class Price")
        _class = Classe.objects.create(name="Trumpet Intermediate", instrument=instrument, price=price)
        class_pack_class = ClassPackClasse.objects.create(class_pack=class_pack, _class=_class)
        assert str(class_pack_class) == "Class Pack C - Trumpet Intermediate"