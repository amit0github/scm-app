# Supply Chain Management (SCM) Application

A Django-based web application for managing construction/civic projects. This system connects Local Councils, Management Companies, and Contractors to streamline project creation, assignment, and bidding.

## Features

*   **Role-Based Access Control**:
    *   **Local Council**: Create projects, assign management companies, view all project details.
    *   **Management Company**: Oversee assigned projects, review bids.
    *   **Contractor**: Browse open projects, place bids on specific requirements.
*   **Project Management**: Create projects with multiple specific requirements (e.g., Excavation, Traffic Management).
*   **Bidding System**: Contractors can submit bids for specific project requirements.
*   **Dashboard**: Role-specific dashboards showing relevant projects and actions.
*   **Responsive Design**: Built with **Bulma CSS** for a clean, modern UI.

## Prerequisites

*   Python 3.10 or higher
*   pip (Python package installer)

## Installation Guide

Follow these steps to set up the project locally.

### 1. Clone or Download the Project
Download the project files to your local machine (`scm_app` folder).

### 2. Set Up a Virtual Environment
It is recommended to use a virtual environment to manage dependencies.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Install Django and other required packages using `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations
Initialize the SQLite database and create the necessary tables.

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Admin)
Create an admin account to manage users and access the Django admin panel.

```bash
python manage.py createsuperuser
```
Follow the prompts to set a username, email, and password.

### 6. Run the Development Server
Start the local server to run the application.

```bash
python manage.py runserver
```

Open your web browser and navigate to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## How to Use

### 1. Registration
*   Go to the **Register** page.
*   Create accounts for different roles:
    *   Select **Local Council** to test project creation.
    *   Select **Management Company** to test project assignment.
    *   Select **Contractor** to test bidding.

### 2. Workflow Example
1.  **Council**: Log in as a Council member. Click "Create Project". Fill in details and add requirements (e.g., "Road Resurfacing"). You can assign a Management Company here.
2.  **Contractor**: Log in as a Contractor. Go to "Projects" or your Dashboard. View a project and click "Place Bid" on a requirement.
3.  **Review**: Log in as the Council or Assigned Company. Go to the Project Detail page. You will see the list of bids submitted by contractors.

## Project Structure

*   `manage.py`: Django's command-line utility.
*   `scm_project/`: Project configuration (settings, URLs).
*   `core/`: Main application logic.
    *   `models.py`: Database definitions (User, Project, Bid).
    *   `views.py`: Application logic and page rendering.
    *   `forms.py`: Forms for user input.
    *   `urls.py`: URL routing for the app.
*   `templates/`: HTML files for the user interface.
