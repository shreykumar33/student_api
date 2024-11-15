#endpoint
#from django.urls import path
#urls pattern

from django.urls import path
from .views import StudentsAPI, StudentsbyIdAPI, student_summary_view

urlpatterns = [

    path('students/',StudentsAPI.as_view() ),
    path('students/<int:student_id>/',StudentsAPI.as_view() ),
    path('student-id/<int:id>/',StudentsbyIdAPI.as_view() ),
    path('students/<int:id>/summary/', student_summary_view, name='student_summary'),
    
    
]