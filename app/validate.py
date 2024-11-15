from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status
import re

def validate_data(student_data, is_put = False, students= None, student_id= None):
   

    age = student_data.get('age')
    name = student_data.get('name')
    email = student_data.get('email')
    number = student_data.get('number')

    errors = []    

    if students is None:
        students = {}

    

    if number:
        if any(student['number'] == number and (student_id != student['id'] if student_id else True) for student in students.values()):
            errors.append(f"Number '{number}' is already taken!")

    if name is not None:
        if not isinstance(name, str) or len(name.strip()) == 0:
            errors.append("Name must be a non-empty string!")
        elif len(name) < 2:
            errors.append("Name must be at least 2 characters long!")

    
    if email:
        if not isinstance(email, str) or len(email.strip()) == 0:
            errors.append("Email cannot be empty or only spaces!")
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            errors.append("Email must be a valid email address!")


    if number is not None:
        if not isinstance(number, str) or len(number.strip()) != 10:
            errors.append("Number must be at 10 digits long!")
        elif not number.isdigit():
            errors.append("Number must be numeric!")

    if age is not None:
        if not isinstance(age, int):
            errors.append("Age must be a valid integer!")
        elif age <= 0:
            errors.append("Age must be a positive integer!")
        elif age > 70:
            errors.append("Age cannot be greater than 70!")


    if not is_put:
        if not name:
            errors.append("Name is required!")
        if not email:
            errors.append("Email is required!")
        if not number:
            errors.append("Number is required!")
        if age is None:
            errors.append("Age is required!")

    if errors:
        raise ValidationError({"errors": errors})

    return True