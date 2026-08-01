# 🍳 Recipe Saver

A web application built with **Python and Django** that allows users to create, save, and manage their favorite recipes in one place.

## 📌 About the Project

**Recipe Saver** is a Django-based recipe management application designed to make it easy to store and organize recipes.

Users can add recipes by entering details such as the recipe name, ingredients, and preparation instructions. Saved recipes can then be viewed and managed from the application.

This project was created to practice **Django web development, database management, CRUD operations, templates, forms, and deployment**.

## ✨ Features

* 📝 Add new recipes
* 📖 View saved recipes
* ✏️ Edit existing recipes
* 🗑️ Delete recipes
* 🥕 Store ingredients and cooking instructions
* 🗂️ Organize recipes in one place
* 🌐 Web-based interface
* 💾 Database-backed recipe storage

## 🛠️ Technologies Used

* **Python**
* **Django**
* **HTML**
* **CSS**
* **SQLite**
* **Git & GitHub**
* **Render** – Deployment

## 📂 Project Structure

```text
Recipe-Saver/
│
├── manage.py
├── requirements.txt
├── db.sqlite3
│
├── project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
│
├── recipes/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   └── urls.py
│
└── static/
    └── ...
```

## ⚙️ How to Run Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### 2. Navigate to the project folder

```bash
cd Recipe-Saver
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply migrations

```bash
python manage.py migrate
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open the application in your browser at:

```text
http://127.0.0.1:8000/
```

## 🗄️ Database

The project uses **SQLite** during development.

Django's ORM is used to create, retrieve, update, and delete recipe data from the database.

## 🚀 Deployment

The project can be deployed using **Render** with Django's production settings, including:

* `ALLOWED_HOSTS`
* `STATIC_ROOT`
* Static file configuration
* `requirements.txt`
* Production WSGI configuration

## 🎯 What I Learned

Through this project, I practiced:

* Django project and app creation
* Django URL routing
* Models and Django ORM
* Database migrations
* Django forms
* CRUD operations
* HTML templates
* Static files
* Git and GitHub
* Deploying a Django application

## 🔮 Future Improvements

Some features that could be added in the future:

* 👤 User registration and login
* ❤️ Favorite recipes
* 🔍 Recipe search
* 🏷️ Categories and tags
* 📷 Recipe image uploads
* 📱 Improved mobile responsiveness
* 🔐 User-specific private recipes
* ⭐ Recipe ratings and reviews

## 👩‍💻 Author

**Tanishka Rajendra Borawake**

BTech – Electronics and Telecommunication Engineering
Deogiri Institute of Engineering and Management Studies

---

⭐ If you find this project useful, consider giving the repository a star!
