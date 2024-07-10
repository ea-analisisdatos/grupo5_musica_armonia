# En admin.py de tu app
from django.contrib import admin
from .models import Teacher, ClassPack, Instrument, Price, Classe, Level, TeacherClasse, Student, Enrollment, ClassPackDiscountRules, ClassPackClasse

admin.site.register(Teacher)
admin.site.register(ClassPack)
admin.site.register(Instrument)
admin.site.register(Price)
admin.site.register(Classe)
admin.site.register(Level)
admin.site.register(TeacherClasse)
admin.site.register(Student)
admin.site.register(Enrollment)
admin.site.register(ClassPackDiscountRules)
admin.site.register(ClassPackClasse)
