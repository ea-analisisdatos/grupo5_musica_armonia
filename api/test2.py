import pytest
from rest_framework.test import APIClient
from .models import Teacher, ClassPack, Instrument, Price, Class, Level, TeacherClass, Student, Enrollment, ClassPackDiscount, ClassPackClass

@pytest.mark.django_db
def test_create_teacher():
    client = APIClient()
    response = client.post('/api/teachers/', {'name': 'John Doe'}, format='json')
    assert response.status_code == 201
    assert Teacher.objects.count() == 1

@pytest.mark.django_db
def test_create_class_pack():
    client = APIClient()
    response = client.post('/api/class_packs/', {'name': 'Pack 1'}, format='json')
    assert response.status_code == 201
    assert ClassPack.objects.count() == 1

@pytest.mark.django_db
def test_create_instrument():
    client = APIClient()
    response = client.post('/api/instruments/', {'name': 'Piano'}, format='json')
    assert response.status_code == 201
    assert Instrument.objects.count() == 1

@pytest.mark.django_db
def test_create_price():
    client = APIClient()
    response = client.post('/api/prices/', {'amount': 100.00, 'description': 'Price 1'}, format='json')
    assert response.status_code == 201
    assert Price.objects.count() == 1

@pytest.mark.django_db
def test_create_class():
    instrument = Instrument.objects.create(name='Piano')
    price = Price.objects.create(amount=100.00, description='Price 1')
    client = APIClient()
    response = client.post('/api/classes/', {'name': 'Class 1', 'instrument': instrument.id, 'price': price.id}, format='json')
    assert response.status_code == 201
    assert Class.objects.count() == 1

@pytest.mark.django_db
def test_create_level():
    class_related = Class.objects.create(name='Class 1', instrument=Instrument.objects.create(name='Piano'), price=Price.objects.create(amount=100.00, description='Price 1'))
    client = APIClient()
    response = client.post('/api/levels/', {'name': 'Level 1', 'class_related': class_related.id}, format='json')
    assert response.status_code == 201
    assert Level.objects.count() == 1

@pytest.mark.django_db
def test_create_teacher_class():
    teacher = Teacher.objects.create(name='John Doe')
    class_related = Class.objects.create(name='Class 1', instrument=Instrument.objects.create(name='Piano'), price=Price.objects.create(amount=100.00, description='Price 1'))
    client = APIClient()
    response = client.post('/api/teacher_classes/', {'teacher': teacher.id, 'class_related': class_related.id}, format='json')
    assert response.status_code == 201
    assert TeacherClass.objects.count() == 1

@pytest.mark.django_db
def test_create_student():
    client = APIClient()
    response = client.post('/api/students/', {'first_name': 'Jane', 'last_name': 'Doe', 'age': 20}, format='json')
    assert response.status_code == 201
    assert Student.objects.count() == 1

@pytest.mark.django_db
def test_create_enrollment():
    student = Student.objects.create(first_name='Jane', last_name='Doe', age=20)
    class_related = Class.objects.create(name='Class 1', instrument=Instrument.objects.create(name='Piano'), price=Price.objects.create(amount=100.00, description='Price 1'))
    teacher = Teacher.objects.create(name='John Doe')
    level = Level.objects.create(name='Level 1', class_related=class_related)
    client = APIClient()
    response = client.post('/api/enrollments/', {'student': student.id, 'class_related': class_related.id, 'teacher': teacher.id, 'level': level.id, 'enrollment_date': '2024-07-06', 'class_number': 1}, format='json')
    assert response.status_code == 201
    assert Enrollment.objects.count() == 1

@pytest.mark.django_db
def test_create_class_pack_discount():
    class_pack = ClassPack.objects.create(name='Pack 1')
    class_related = Class.objects.create(name='Class 1', instrument=Instrument.objects.create(name='Piano'), price=Price.objects.create(amount=100.00, description='Price 1'))
    client = APIClient()
    response = client.post('/api/class_pack_discounts/', {'class_pack': class_pack.id, 'class_related': class_related.id, 'discount_percentage': 10.00}, format='json')
    assert response.status_code == 201
    assert ClassPackDiscount.objects.count() == 1

@pytest.mark.django_db
def test_create_class_pack_class():
    class_pack = ClassPack.objects.create(name='Pack 1')
    class_related = Class.objects.create(name='Class 1', instrument=Instrument.objects.create(name='Piano'), price=Price.objects.create(amount=100.00, description='Price 1'))
    client = APIClient()
    response = client.post('/api/class_pack_classes/', {'class_pack': class_pack.id, 'class_related': class_related.id}, format='json')
    assert response.status_code == 201
    assert ClassPackClass.objects.count() == 1