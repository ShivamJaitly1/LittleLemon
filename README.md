# **Little Lemon Web App**  
The **Little Lemon Web App** is a restaurant management platform that allows users to manage menu items, handle bookings, and authenticate themselves to access restricted resources. It is built using **Django** for the backend and **Django REST Framework (DRF)** for API functionalities.  

---

## **Features**  
✅ **Menu Management** – Add, view, and manage menu items.  
✅ **Booking Management** – Make and manage bookings for customers.  
✅ **Authentication** – Users can sign up, log in, and access protected API endpoints.  
✅ **API Access** – Exposes RESTful APIs for interacting with menu and booking data.  
✅ **Testing** – Pre-configured unit tests ensure the reliability of features.  

---

## **Technologies Used**  
- **Django** – High-level Python web framework for backend development.  
- **Django REST Framework (DRF)** – Powerful toolkit for building APIs in Django.  
- **Djoser** – Handles user authentication with token-based authentication.  
- **MySQL** – Stores app data, including menu items and bookings.  
- **Insomnia/Postman** – Tools for testing APIs.  

---

## **Installation**  

### **1. Clone the repository**  
```bash
git clone <repository-url>
cd little-lemon
```

### **2. Create a virtual environment and activate it**  
```bash
python -m venv venv  
source venv/bin/activate  # On macOS/Linux  
venv\Scripts\activate     # On Windows  
```

### **3. Install dependencies**  
```bash
pip install -r requirements.txt  
```

### **4. Set up the database**  
- Configure your **MySQL database settings** in `settings.py` under `DATABASES`.  

### **5. Run migrations**  
```bash
python manage.py migrate  
```

### **6. Create a superuser to access Django Admin**  
```bash
python manage.py createsuperuser  
```

### **7. Run the development server**  
```bash
python manage.py runserver  
```

---

## **Testing the API**  
You can test the API using **Insomnia** or **Postman**.  

### **Endpoints:**  
🔹 **Menu API:** `/api/menu/` (GET, POST)  
🔹 **Booking API:** `/api/bookings/` (GET, POST)  
🔹 **User Authentication:**  
  - Login: `/auth/token/login/`  
  - Logout: `/auth/token/logout/`  

🔹 **Authentication:**  
To authenticate a user, obtain the token from `/auth/token/login/` and include it in the **Authorization header** as `Bearer <your_token>` for subsequent requests.  

---

## **Unit Testing**  
Unit tests are written using Django’s `TestCase` class. To run the tests, use:  
```bash
python manage.py test  
```

---

