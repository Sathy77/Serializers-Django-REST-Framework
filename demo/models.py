from django.db import models

# Create your models here.

class Depertment (models.Model):
    dname = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.dname 
    
class Course (models.Model):
    cname = models.CharField(max_length=100, blank=True, null=True)
    

    def __str__(self):
        return self.cname 

class Advisor(models.Model):
    aname = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    deperment = models.ForeignKey(Depertment, on_delete=models.CASCADE, blank=True, null=True, related_name="advisor")
    course = models.ManyToManyField(Course, blank=True, null=True)
    
    def __str__(self):
        return self.aname
    


class Student (models.Model) :
    sname = models.CharField(max_length=100, blank=True, null=True)
    deperment = models.ForeignKey(Depertment, on_delete=models.CASCADE, blank=True, null=True, related_name="student")
    advisor = models.ForeignKey(Advisor, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ManyToManyField(Course, blank=True, null=True)

    def __str__(self):
        return self.sname
