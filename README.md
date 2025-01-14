# Effective Mobile Task Project | Restaurant

## Project Overview

This Django project is designed
to help to manage restaurant order management system. Ordinary users can see order data, managers can manage 
orders. It is built using the Django framework and follows best practices for web development,
including modular design, scalability, and security.

## Prerequisites

- Python 3.8+
- Django 5.x
- A database system (e.g., SQLite, PostgreSQL)
- [Any additional requirements, e.g., Docker]

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SanjarbekAI/effectivemobile.git
   cd effectivemobile
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate   # For Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
    - Create a `.env` file in the root directory.
    - Add the following variables:
      ```env
      SECRET_KEY=your_secret_key
      DEBUG=True
      ```

5. **Apply migrations**:

   ```bash
   python manage.py migrate
   ```

6**Apply translation**:

   ```bash
   python manage.py compilemessages
   ```

6. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

7. **Access the application**: Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Testing

1. **Run unit tests**:
   ```bash
   python manage.py test
   ```
