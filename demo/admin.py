from django.contrib import admin

# Register your models here.

from demo.models import Advisor, Student, Depertment, Course 

admin.site.register({Advisor, Student, Depertment, Course})
