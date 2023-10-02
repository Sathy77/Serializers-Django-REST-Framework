from rest_framework import serializers
from demo.models import *

class DepertmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Depertment
		fields =['dname']

# id soho print korbe
#class CourseSerializerid(serializers.ModelSerializer):
#	class Meta:
#		model = Course
#		fields ='__all__'
		
class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields =['cname']
		
class AdvisorSerializer(serializers.ModelSerializer):
	course=CourseSerializer(many=True)
	deperment=DepertmentSerializer(many=False)
	class Meta:
		model = Advisor
		fields ='__all__'
		
class StudentSerializer(serializers.ModelSerializer):
	course=CourseSerializer(many=True)
	deperment=DepertmentSerializer(many=False)
	advisor=AdvisorSerializer(many=False)
	class Meta:
		model = Student
		fields ='__all__'