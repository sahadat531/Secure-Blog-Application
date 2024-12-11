# Secure Blog Application

Welcome to the **Secure Blog Application**, a Django-based project that demonstrates secure web application development. This application includes best practices for coding securely, handling user authentication, and preventing vulnerabilities like SQL Injection and Cross-Site Scripting (XSS).

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Security Practices](#security-practices)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview

The **Secure Blog Application** is a simple blogging platform where users can:
- View blog posts.
- Create new blog posts (authenticated users only).
- Ensure data security through secure coding practices.

This project serves as a demonstration of secure application development for educational and professional purposes.

---

## Features

- **User Authentication**: Login required to create posts.
- **Secure Input Handling**: Validations and protections against malicious inputs.
- **CSRF Protection**: Cross-Site Request Forgery prevention enabled.
- **Responsive UI**: Basic templates for easy use.

---

## Project Structure

```
secure_blog/
|
├── secure_blog/
│   ├── settings.py        # Project settings (security-focused)
│   ├── urls.py            # URL routing
│   ├── wsgi.py            # WSGI configuration
│
├── blog/
│   ├── models.py          # Database models for blog posts
│   ├── views.py           # Views for blog functionalities
│   ├── forms.py           # Forms for handling user input
│   ├── templates/blog/    # HTML templates
│
├── db.sqlite3             # SQLite database
├── manage.py              # Django management commands
└── README.md              # Project documentation
```

---

## Setup and Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/secure_blog.git
   cd secure_blog
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install django
   ```

4. **Run Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   Open your browser and visit `http://127.0.0.1:8000/`.

---

## Usage

- **Home Page**: View existing blog posts.
- **Create Post**: Authenticated users can create a new blog post.

---

## Security Practices

- **Input Validation**: User input is validated to prevent SQL Injection and XSS attacks.
- **CSRF Protection**: Enabled by default in Django.
- **Secure Authentication**: Passwords are hashed using Django's built-in system.
- **HTTPS Ready**: Configured for secure communication in production.

---

## Screenshots

### 1. Home Page
![Home Page Screenshot](https://via.placeholder.com/800x400?text=Home+Page)

### 2. Create Post
![Create Post Screenshot](https://via.placeholder.com/800x400?text=Create+Post)

---

## Contributing

Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Create a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For any questions or feedback, feel free to reach out:
- **Email**: sahadathossensajib@gmail.com
- **LinkedIn**: [Sahadat Hossen Sajib](https://www.linkedin.com/in/sahadatsajib/)

