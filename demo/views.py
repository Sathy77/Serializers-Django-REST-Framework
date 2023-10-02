from django.shortcuts import render
from demo.models import *
from demo.api.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def depermentList(request):
	deperments = Depertment.objects.all()
	depertmentserializer = DepertmentSerializer(deperments, many=True)
	return Response(depertmentserializer.data)


@api_view(['GET'])
def courselist(request):
	courses = Course.objects.all()
	courseserializer=CourseSerializer(courses, many=True)
	# courseserializer=CourseSerializerid(courses, many=True)
	return Response(courseserializer.data)


@api_view(['GET'])
def advisorlist(request):
	advisors = Advisor.objects.all()
	advisorserializer = AdvisorSerializer(advisors, many=True)
	return Response(advisorserializer.data)

@api_view(['GET'])
def studentlist(request):
	students =  Student.objects.all()
	studentserializer = StudentSerializer(students, many=True)
	return Response(studentserializer.data)