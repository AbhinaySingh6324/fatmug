# Project Setup Instructions
deployed-Link https://fatmug.onrender.com
Follow these steps to set up and run the project locally:

1. **Clone the Repository:**
   - Clone the project repository from GitHub to your local machine:
     ```bash
     git clone <repository_url>
     ```

2. **Navigate to the Project Directory:**
   - Change your current directory to the root directory of the cloned project:
     ```bash
     cd <project_directory>
     ```

3. **Install Dependencies:**
   - Install the required Python dependencies using pip:
     ```bash
     pip install -r requirements.txt
     ```

4. **Set Up Database:**
   - Configure your database settings in the project's settings.py file.
   - Run the database migrations to create the database schema:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

5. **Run the Development Server:**
   - Start the Django development server to run the project locally:
     ```bash
     python manage.py runserver
     ```

6. **Access the API Endpoints:**
   - Once the development server is running, you can access the API endpoints using your web browser or a tool like Postman. Use the specified URLs and methods to interact with the API.

7. **Create Superuser (Optional):**
   - If you need administrative access to the Django admin interface, create a superuser account:
     ```bash
     python manage.py createsuperuser
     ```
   - Follow the prompts to provide a username, email, and password for the superuser account.

8. **Additional Configuration:**
   - Depending on your project requirement


# Vendor APIs  - "api/" subroute for other functional routes.

## Vendor List/Create
- **URL:** `/api/vendors/`
- **Method:** GET, POST
- **Description:** Retrieve a list of vendors or create a new vendor.
- **Permissions:** Public
- **Response:** JSON array of vendor objects.

## Vendor Retrieve/Update/Destroy
- **URL:** `/api/vendors/<vendor_id>/`
- **Method:** GET, PUT, DELETE
- **Description:** Retrieve, update, or delete a specific vendor.
- **Permissions:** Public
- **Response:** JSON object of the vendor.

## Purchase Order List/Create
- **URL:** `/api/purchase-orders/`
- **Method:** GET, POST
- **Description:** Retrieve a list of purchase orders or create a new purchase order.
- **Permissions:** Public
- **Response:** JSON array of purchase order objects.

## Purchase Order Retrieve/Update/Destroy
- **URL:** `/api/purchase-orders/<purchase_order_id>/`
- **Method:** GET, PUT, DELETE
- **Description:** Retrieve, update, or delete a specific purchase order.
- **Permissions:** Public
- **Response:** JSON object of the purchase order.

## Vendor Performance
- **URL:** `/api/vendors/<vendor_id>/performance/`
- **Method:** GET
- **Description:** Retrieve historical performance metrics for a specific vendor.
- **Permissions:** Public
- **Response:** JSON array of performance metrics.

# User Authentication APIs

## Sign Up
- **URL:** `/api/signup/`
- **Method:** POST
- **Description:** Create a new user account.
- **Permissions:** Only authenticated users
- **Request Data:** User details including email, username, and password.
- **Response:** Success message with user data.

## Login
- **URL:** `/api/login/`
- **Method:** POST
- **Description:** Authenticate and login a user.
- **Permissions:** Public
- **Request Data:** User's email and password.
- **Response:** Success message with authentication tokens.

## User Profile
- **URL:** `/api/user-profile/`
- **Method:** GET
- **Description:** Retrieve the authenticated user's profile.
- **Permissions:** Only authenticated users
- **Response:** JSON object of the user's profile.
