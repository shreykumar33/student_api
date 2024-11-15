
# FealtyX API

The FealtyX API is a RESTful application designed to manage student records, including functionalities to create, read, update, and delete student data. The API includes robust validation mechanisms to ensure data integrity and provides endpoints to retrieve summaries of student information.

## Features
- **CRUD Operations**:
  - **Create**: Add new student records.
  - **Read**: Fetch all or specific student records.
  - **Update**: Modify existing student records.
  - **Delete**: Remove student records.
- **Validation**:
  - Ensures unique constraints on email, phone number, and ID.
  - Validates fields such as `name`, `age`, `email`, and `number` with clear error messages.
- **Summary Generation**:
  - Generate brief summaries of student data using AI (Ollama integration).
- **Thread-Safe**:
  - Uses threading locks to manage concurrent access to the student records.

---

## Technologies Used
- **Framework**: Django Rest Framework (DRF)
- **Language**: Python
- **Validation**: Custom validation logic with `ValidationError` from DRF.
- **Concurrency**: Threading locks for thread-safe operations.
- **External Integration**: Ollama AI for summary generation.

---

## Installation and Setup

### Prerequisites
- Python 3.8+
- Django 3.2+
- pip (Python package manager)

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fealtyx-api.git
   cd fealtyx-api
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the server:
   ```bash
   python manage.py runserver
   ```

---

## Endpoints

### **1. Students Endpoints**
#### Fetch all students
- **URL**: `/api/students/`
- **Method**: `GET`
- **Response**:
  ```json
  [
    {
      "id": 1,
      "name": "John Doe",
      "age": 25,
      "email": "john.doe@example.com",
      "number": "1234567890"
    }
  ]
  ```

#### Add a new student
- **URL**: `/api/students/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "age": 25,
    "email": "john.doe@example.com",
    "number": "1234567890"
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "age": 25,
    "email": "john.doe@example.com",
    "number": "1234567890"
  }
  ```

#### Update an existing student
- **URL**: `/api/students/<student_id>`
- **Method**: `PUT`
- **Request Body**:
  ```json
  {
    "name": "Jane Doe",
    "age": 22
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "name": "Jane Doe",
    "age": 22,
    "email": "john.doe@example.com",
    "number": "1234567890"
  }
  ```

#### Delete a student
- **URL**: `/api/students/<student_id>`
- **Method**: `DELETE`
- **Response**:
  ```json
  {
    "message": "Student John Doe deleted successfully!"
  }
  ```

---

### **2. Student By ID Endpoint**
#### Fetch a specific student by ID
- **URL**: `/api/student-id/<id>`
- **Method**: `GET`
- **Response**:
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "age": 25,
    "email": "john.doe@example.com",
    "number": "1234567890"
  }
  ```

---

### **3. Student Summary Endpoint**
#### Generate a summary of all students
- **URL**: `/api/student_summary/`
- **Method**: `GET`
- **Response**:
  ```json
  {
    "summary": "There are 10 students with an average age of 22. The most common names are John and Jane."
  }
  ```

---

## Validation Rules
- **Name**:
  - Must be a non-empty string with at least 2 characters.
- **Email**:
  - Must be a valid email format.
  - Must be unique across all records.
- **Number**:
  - Must be a 10-digit numeric string.
  - Must be unique across all records.
- **Age**:
  - Must be a positive integer not greater than 70.

---

## File Structure
```
fealtyx-api/
│
├── app/
│   ├── views.py          # API views and logic
│   ├── validate.py       # Validation logic
│   ├── urls.py           # Endpoint routing
│   └── ...
├── manage.py             # Django management script
└── requirements.txt      # Project dependencies
```

---

## Example Usage
### Create a New Student
1. Send a POST request to `/api/students/` with the student's details:
   ```bash
   curl -X POST http://127.0.0.1:8000/api/students/    -H "Content-Type: application/json"    -d '{"name": "Alice", "age": 23, "email": "alice@example.com", "number": "9876543210"}'
   ```

2. The server will respond with:
   ```json
   {
     "id": 2,
     "name": "Alice",
     "age": 23,
     "email": "alice@example.com",
     "number": "9876543210"
   }
   ```

---

