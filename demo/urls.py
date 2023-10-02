from django.urls import path
from demo.views import *

urlpatterns = [

    path('deperment-list/', depermentList, name='deperment-list'),
    path('course-list/', courselist, name='course-list'),
    path('advisor-list/', advisorlist, name='advisor-list'),
    path ('student-list/', studentlist, name='student-list'),
    ]