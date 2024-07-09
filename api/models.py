from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Teachers'

class ClassPack(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Class_Packs'

class Instrument(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Instruments'

class Price(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.amount} - {self.description}"

    class Meta:
        db_table = 'Prices'

class Classes(models.Model):
    name = models.CharField(max_length=100)
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    price = models.ForeignKey(Price, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Classes'

class Levels(models.Model):
    name = models.CharField(max_length=100)
    _class = models.ForeignKey(Classes, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self._class.name}"

    class Meta:
        db_table = 'Levels'

class TeacherClasses(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    _class = models.ForeignKey(Classes, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.teacher.name} - {self._class.name}"

    class Meta:
        db_table = 'Teacher_Classes'

class Students(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    family_discount = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'Students'

class Enrollments(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    _class = models.ForeignKey(Classes, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True, null=True)
    level = models.ForeignKey(Levels, on_delete=models.CASCADE, blank=True, null=True)
    enrollment_date = models.DateField()
    class_number = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - {self._class.name}"

    class Meta:
        db_table = 'Enrollments'

class ClassPackDiscountRules(models.Model):
    class_pack = models.ForeignKey(ClassPack, on_delete=models.CASCADE)
    class_number = models.IntegerField()
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.class_pack.name} - {self.class_number}"

    class Meta:
        db_table = 'Class_Pack_Discount_Rules'

class ClassPackClasses(models.Model):
    class_pack = models.ForeignKey(ClassPack, on_delete=models.CASCADE)
    _class = models.ForeignKey(Classes, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.class_pack.name} - {self._class.name}"

    class Meta:
        db_table = 'Class_Pack_Classes'
