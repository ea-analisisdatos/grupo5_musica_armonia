# En admin.py de tu app
from django.contrib import admin
from .models import Teacher, ClassPack, Instrument, Price, Classes, Levels, TeacherClasses, Students, Enrollments, ClassPackDiscountRules, ClassPackClasses

admin.site.register(Teacher)
admin.site.register(ClassPack)
admin.site.register(Instrument)
admin.site.register(Price)
admin.site.register(Classes)
admin.site.register(Levels)
admin.site.register(TeacherClasses)
admin.site.register(Students)
admin.site.register(Enrollments)
admin.site.register(ClassPackDiscountRules)
admin.site.register(ClassPackClasses)
