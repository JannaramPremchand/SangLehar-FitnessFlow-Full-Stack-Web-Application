# **SangLehar FitnessFlow**

## **Project Overview**

**SangLehar FitnessFlow** is a comprehensive web-based Gym Fitness Management System developed using **Django (Python)**, **HTML5**, **CSS**, **JavaScript**, and **MySQL**. This platform aims to modernize and streamline gym operations by automating manual tasks and providing a centralized system for administrators, trainers, members, and guests.

The system helps gym owners, trainers, and members manage various activities such as membership tracking, attendance, workout schedules, payments, **eCommerce for gym products**, and product management. It also enhances the user experience with personalized workout plans, diet charts, and engagement features like fitness blogs and videos.

## **Key Features**

### **Admin Module**
- **User Management**: Add, update, or remove users (Admins, Trainers, Members, Guests).
- **Membership Management**: Manage member registration, membership plans, renewals, and cancellations.
- **Attendance Management**: Track attendance records of members and trainers.
- **Payment Management**: Handle membership fees and track payment statuses.
- **Product Management**: Manage gym products (e.g., supplements, gym equipment) and update inventory.
- **Workout Management**: Upload workout schedules, diet plans, and fitness videos for members.
- **Reports**: Generate detailed reports on user activities, payments, memberships, attendance, and feedback.

### **Trainer Module**
- **Workout Schedule Creation**: Create and assign personalized workout schedules for members.
- **Diet Chart Preparation**: Provide custom diet plans based on members' goals and fitness levels.
- **Attendance Tracking**: View attendance records of members and track their own attendance.
- **Video Uploads**: Upload workout tutorials and exercise demonstrations to help members follow routines.
- **Reward Management**: Assign reward points to members based on their weekly performance and consistency.

### **Member Module**
- **Profile Management**: Update personal details such as name, address, email, and phone number.
- **Workout Access**: View and download assigned workout schedules and diet charts.
- **Attendance Records**: Check attendance history to monitor gym visits.
- **Product Purchases**: Browse and purchase gym-related products (e.g., supplements, equipment).
- **Membership Payments**: Renew memberships and track payment history.
- **Feedback Submission**: Provide feedback about the gym and trainers to improve services.

### **Guest Module**
- **Website Exploration**: Browse the gym's website to view services, facilities, and products.
- **FAQs and Testimonials**: Read frequently asked questions and member testimonials.
- **Membership Registration**: Apply for gym membership by filling out a registration form and uploading payment details.
- **Contact Us**: Access gym contact information to inquire further about services.

### **Products (eCommerce) Module**
The Products module allows members and guests to browse and purchase various gym-related products, such as supplements, fitness equipment, clothing, etc.

- **Product Listings**: View a catalog of gym products, including details like price, availability, and description.
- **Shopping Cart**: Add products to the cart, update quantities, or remove items.
- **Product Search and Filters**: Search for products by categories (e.g., supplements, equipment) and apply filters like price range, brand, etc.
- **Order Management**: Place orders and track the status of their purchase.
- **Payment Gateway Integration**: Secure payment integration for purchasing products directly through the platform.
- **Order History**: View purchase history and order details.

## **System Configuration**

- **Operating System**: Windows/Linux/macOS
- **Processor**: Intel i3 or higher
- **RAM**: 4GB or above
- **Storage**: 20GB free space
- **Browser**: Chrome, Firefox, or Edge

## **Software Requirements**

- **Frontend**: HTML5, CSS, JavaScript
- **Backend**: Python 3.8 with Django 3.1
- **Database**: MySQL 5.5
- **Additional Tools**:
  - Microsoft PowerPoint 2019 (for presentation)
  - EDraw Max 9.0 (for diagrams)
  - Microsoft Visio 2016 (for ER diagrams)
  - Microsoft Word 2019 (for documentation)

## **Technologies Used**

- **Frontend**: HTML5, CSS, JavaScript
- **Backend Framework**: Django 3.1
- **Database**: MySQL

## **Key Features**

- **Automated attendance and membership tracking**.
- **Personalized workout schedules and diet charts for members**.
- **Product management and online shopping for gym equipment**.
- **Fitness blogs, videos, and reward systems to enhance member engagement**.
- **Comprehensive reporting and filtering for user, attendance, and payment data**.

## **Getting Started**

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

