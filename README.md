# Full-Stack-Gym-Web-App

## **Project Description**

This project is a web application for a fitness center. It allows users to sign up, log in, and view gym information. It also provides a gym schedule and membership plans.

## **Project Setup Guide**

Follow these steps to set up the project on your local machine:

### **1. Clone the Repository**
```bash
git clone https://github.com/JannaramPremchand/Full-Stack-Gym-Web-App.git
cd Full-Stack-Gym-Web-App
```

### **2. Create a Virtual Environment**
Create and activate a Python virtual environment to manage dependencies.

- **On Windows:**
  ```bash
    pip install virtualenv
    python -m venv env
    .\env\Scripts\activate
    pip install -r requirements.txt
  ```

### **3. Install Dependencies**
Install the required Python packages using `requirements.txt`:
```bash
pip install -r requirements.txt
```

### **4. Apply Database Migrations**
Set up the database by applying migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### **5. Create a Superuser**
Create an admin account to access the Django admin panel:
```bash
python manage.py createsuperuser
```
Follow the prompts to set a username, email, and password.

### **6. Run the Development Server**
Start the development server:
```bash
python manage.py runserver
```

The website will be accessible at:  
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

### **7. Access the Admin Panel**
Visit the admin panel at:  
[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)  
Log in with the superuser credentials you created.

