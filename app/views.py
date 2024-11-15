# myapp/views.py

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from threading import Lock
from .validate import validate_data
from rest_framework.exceptions import ValidationError
import ollama

students = {}
next_id = 1

students_lock = Lock()


class StudentsAPI(APIView):
    def get(self, request):
        try:
           
            global students
            
            return Response(list(students.values()), status=status.HTTP_200_OK)

        except Exception as e:
           return Response({'error': str(e)})


    def post(self, request):
        global students, next_id
        
        student_data = request.data
        validate_data(student_data, is_put=False, students= students)

        '''
        
        age = request.data.get('age') 
        name= request.data.get('name')
        email= request.data.get('email')

        

        if not name:
            return Response({'error': "Name is required!"}, status=status.HTTP_400_BAD_REQUEST)

        if not age:
            return Response({'error': "Age is required!"}, status=status.HTTP_400_BAD_REQUEST)

        if not age:
            return Response({'error': "Age is required!"}, status=status.HTTP_400_BAD_REQUEST)

        if age:
            if type(age) != int:
                return Response({'error': "Enter valid age!"}, status=status.HTTP_400_BAD_REQUEST)

'''
        #if not age.isdigit():
         #   return Response({'error': 'enter a valid number'}, status=status.HTTP_400_BAD_REQUEST)
        with students_lock:
            student = {
                'id': len(students)+1,
                'name': student_data.get('name'),
                'age': student_data.get('age'),
                'number': student_data.get('number'),
                'email': student_data.get('email')

            }
            students[next_id] = student
            next_id += 1
            return Response(student, status=status.HTTP_201_CREATED)

    def put(self, request, student_id):
        global students
        
        student_data = request.data

        try:
            validate_data(student_data, is_put=True, students= students,  student_id= student_id)
        except ValidationError as e:
            return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)
        with students_lock:

            if student_id in students:
                students[student_id]['id'] = student_data.get('id', students[student_id]['id'])
                students[student_id]['name'] = student_data.get('name', students[student_id]['name'])
                students[student_id]['age'] = student_data.get('age', students[student_id]['age'])
                students[student_id]['email'] = student_data.get('email', students[student_id]['email'])
                return Response(students[student_id], status=status.HTTP_200_OK)
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, student_id):
        global students
        with students_lock:

            if student_id in students:
                deleted_student = students.pop(student_id)
                return Response({'message': f'Student {deleted_student["name"]} deleted successfully!'}, status=status.HTTP_200_OK)
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

class StudentsbyIdAPI(APIView):
    def get(self, request, id):
        try:
           
            global students

            student = students.get(id)
            if student:
                return Response(student, status=status.HTTP_200_OK)
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
           return Response({'error': str(e)})
        

        
def generate_summary(students):
    message = {
        "role": "user", 
        "content": f"Please generate a brief summary of the following student data: {students}"
    }

    try:
        response = ollama.chat('llama3', messages=[message])
        return response.get('message', {}).get('content', 'No response from Ollama')
    except Exception as e:
        return f"Error generating summary: {e}"


@api_view(['GET'])
def student_summary_view(request):
    student_data = request.data

    if students is None:
        return Response({'error': 'Failed to fetch student data'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    summary = generate_summary(students)
    return Response({'summary': summary}, status=status.HTTP_200_OK)