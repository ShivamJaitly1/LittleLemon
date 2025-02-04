**Little Lemon Web App** <br />
The Little Lemon web app is a restaurant management platform where users can manage menu items, handle bookings, and authenticate themselves to access restricted resources. It is built using Django for the backend and Django REST Framework for API functionalities.
<br />
<br />
<br />
**Features**<br />
  **Menu Management:** Add, view, and manage menu items.<br />
  **Booking Management:** Make and manage bookings for customers.<br />
  **Authentication:** Users can sign up, log in, and access protected API endpoints.<br />
  **API Access:** The app exposes RESTful APIs for interacting with menu and booking data.<br />
  **Testing:** The app comes with pre-configured unit tests to ensure the reliability of the features.<br />
<br />
<br />
<br />
**Technologies Used**<br />
**Django:** A high-level Python web framework for backend development.<br />
**Django REST Framework (DRF):** A powerful toolkit for building APIs in Django.<br />
**Djoser:** A library for handling user authentication with token-based authentication.<br />
**MySQL:** The database used to store app data, including menu items and bookings.<br />
**Insomnia/Postman:** Tools used to test the APIs.<br />
<br />
<br />
<br />
**Installation**<br />
**Clone the repository:**<br />


**Navigate to the project directory:**<br />
cd little-lemon<br />

**Create a virtual environment and activate it:**<br />
python -m venv venv<br />
source venv/bin/activate<br />

**Set up the database:**<br />

**Configure your MySQL database settings in settings.py (under DATABASES).<br />
Run migrations:**<br />
python manage.py migrate<br />

**Create a superuser to access the Django Admin:**<br />
python manage.py createsuperuser<br />

**Run the development server:**<br />
python manage.py runserver<br />

<br />
<br />
<br />

**Testing the API** <br />
You can test the API using tools like Insomnia or Postman. Use the following endpoints for testing:<br />

**Menu API:** /api/menu/ (GET, POST)<br />
**Booking API:** /api/bookings/ (GET, POST)<br />
**User Authentication:** /auth/token/login/, /auth/token/logout/<br />
To authenticate a user, obtain the token from the /auth/token/login/ endpoint and include it in the Authorization header as Bearer <token> in subsequent requests.<br />

**Unit Testing**<br />
Unit tests are written using Django's TestCase class. To run the tests, use the following command:<br />
python manage.py test<br />
