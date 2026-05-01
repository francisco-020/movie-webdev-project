# Movie Website Backend Project

This project is for **CSCI 3342 Project #2**. The goal is to convert a static movie website template into a dynamic Django web application using PostgreSQL and pgAdmin.

## Project Overview

The application will:

- convert static HTML sections into dynamic Django-rendered content
- use PostgreSQL as the database
- use Django models based on the provided ER diagram
- support Django admin for content management
- use template inheritance for cleaner layout structure
- render static assets like CSS, JavaScript, and images
- include a working newsletter form
- support collaborative development through GitHub

## Tech Stack

- Python
- Django
- PostgreSQL
- pgAdmin
- HTML / CSS / JavaScript
- GitHub

## Project Structure

    movie-backend-project/
    ├── config/              # Django project configuration
    ├── movies/              # Main app for models, views, admin, etc.
    ├── manage.py
    ├── requirements.txt
    ├── .env.example         # safe template file for environment variables
    ├── README.md
    └── venv/                # local only, not pushed to GitHub

## Team Setup Instructions

After cloning the repository, each teammate must complete the following setup on their own machine.

### 1. Clone the repository

    git clone <your-repo-url>
    cd movie-backend-project

### 2. Create and activate a virtual environment

#### Git Bash

    py -m venv venv
    source venv/Scripts/activate

#### Command Prompt

    py -m venv venv
    venv\Scripts\activate

#### PowerShell

    py -m venv venv
    venv\Scripts\Activate.ps1

### 3. Install dependencies

    pip install -r requirements.txt

## Local Environment File (`.env`)

Each teammate must create their **own local `.env` file** in the project root.

This file is required for Django to run, but it is **not uploaded to GitHub** because it contains private configuration values such as your Django secret key and PostgreSQL credentials.

The repository includes a file called `.env.example`. That file is only a template to show the structure. Use it to make your own personal `.env`.

### 4. Create your own local `.env` file

Create a new file named `.env` in the project root.

Then copy the structure from `.env.example` and replace the placeholder values with your own local values.

Example:

    DEBUG=True
    SECRET_KEY=your-own-generated-secret-key
    DB_NAME=movie_webdev_project2
    DB_USER=your_postgres_user
    DB_PASSWORD=your_postgres_password
    DB_HOST=localhost
    DB_PORT=5432

### What each variable means

- `DEBUG`  
  Keeps Django in development mode. Leave this as `True` during local development.

- `SECRET_KEY`  
  A private Django security key. Each teammate should generate their **own** secret key.

- `DB_NAME`  
  The name of your local PostgreSQL database for this project.

- `DB_USER`  
  Your local PostgreSQL username.

- `DB_PASSWORD`  
  The password for your local PostgreSQL user.

- `DB_HOST`  
  Usually `localhost` for local development.

- `DB_PORT`  
  Usually `5432` for PostgreSQL.

### Important `.env` rules

- Do **not** commit `.env`
- Do **not** upload real passwords to GitHub
- Do **not** share your real PostgreSQL password in the repo
- Do **not** copy another teammate’s secret key
- Every teammate should use their **own** local `.env`
- The `.env.example` file is safe to upload because it contains only placeholders

### 5. Generate your own Django secret key

Run this command:

    python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

Copy the output and paste it into your `.env` file as the value for `SECRET_KEY`.

## PostgreSQL Setup

Each teammate should set up PostgreSQL on their own machine.

You do **not** need to connect to another teammate’s database. Everyone will have their own local PostgreSQL database, but the Django project structure and tables will stay consistent through migrations.

### 6. Create the PostgreSQL database

In pgAdmin:

- create a database named `movie_webdev_project2`
- create or use a PostgreSQL user you know the password for
- make sure your `.env` matches your own local PostgreSQL setup

Example database values in `.env`:

    DB_NAME=movie_webdev_project2
    DB_USER=movieapp_user
    DB_PASSWORD=your_password_here
    DB_HOST=localhost
    DB_PORT=5432

## Apply Database Migrations

### 7. Run migrations

#### Windows

    python manage.py migrate

#### macOS / Linux

    python3 manage.py migrate

This creates the Django tables in your local PostgreSQL database.

## Load Sample Data

After running migrations, load the shared project data from the fixture file.

### 8. Load the sample data

#### Windows Git Bash, Command Prompt, or PowerShell

    python manage.py loaddata sample_data

#### macOS / Linux

    python3 manage.py loaddata sample_data

This loads the shared movie, slider, social link, celebrity, trailer, news, tweet, and related homepage data into your local PostgreSQL database.

## If You Get a Fixture Encoding Error

On some machines, especially Windows, the `sample_data.json` file may occasionally be saved with the wrong encoding. If that happens, you may see an error similar to:

    UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0

If that happens, convert the fixture file to UTF-8 and then run `loaddata` again.

### Windows fix

Run:

    python -c "from pathlib import Path; p=Path('movies/fixtures/sample_data.json'); text=p.read_text(encoding='utf-16'); p.write_text(text, encoding='utf-8')"

Then run:

    python manage.py loaddata sample_data

### macOS / Linux fix

Run:

    python3 -c "from pathlib import Path; p=Path('movies/fixtures/sample_data.json'); text=p.read_text(encoding='utf-16'); p.write_text(text, encoding='utf-8')"

Then run:

    python3 manage.py loaddata sample_data

### Important note

You only need to use the encoding fix command if the normal `loaddata` command gives the UTF-8 decode error.

If `python manage.py loaddata sample_data` or `python3 manage.py loaddata sample_data` works normally, do not run the encoding fix.

## Create an Admin Account

### 9. Create a superuser

#### Windows

    python manage.py createsuperuser

#### macOS / Linux

    python3 manage.py createsuperuser

Use your own username, email, and password.

## Run the Project

### 10. Start the development server

#### Windows

    python manage.py runserver

#### macOS / Linux

    python3 manage.py runserver

Then open:

    http://127.0.0.1:8000/admin/

Log in with the superuser you created.

## Important Security Notes

Never commit the following:

- `.env`
- database passwords
- Django secret keys
- other private credentials

The repo should only include:

- `.env.example`
- source code
- templates
- migrations
- static files
- documentation

## Collaboration Workflow

To avoid conflicts when working as a team:

- always pull the latest changes before starting work
- create your own branch for a feature or fix
- commit clearly and often
- push your branch to GitHub
- merge changes carefully

Example:

    git checkout -b feature/homepage-models
    git add .
    git commit -m "Add initial homepage models"
    git push origin feature/homepage-models

## Current Project Goal

This project will take the provided static movie template and turn it into a dynamic Django web app by:

- creating models from the ER diagram
- replacing `<!-- DB -->` sections with dynamic content
- organizing templates with inheritance
- registering models in Django admin
- handling static assets correctly
- implementing the newsletter form
