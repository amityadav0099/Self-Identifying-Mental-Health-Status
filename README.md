🧠 Self-Identifying Mental Health Status
A Django-Based Mental Health Self-Assessment Web Application
📌 Overview
The Self-Identifying Mental Health Status project is a simple, secure, and interactive web-based system designed to help users evaluate their mental well-being.
By answering a structured questionnaire, users receive an indicative result such as:

Low Stress / Healthy

Moderate Stress

High Stress

Needs Professional Support

The goal of this project is to promote self-awareness and encourage individuals to understand their emotional and mental state.
This tool is only for educational and awareness purposes, not a medical diagnosis.

🚀 Features
✔ User Registration & Login

✔ Mental Health Questionnaire

✔ Automatic Result Analysis

✔ Clean, Simple & Responsive UI

✔ SQLite Database Integration

✔ Secure Django Authentication

✔ Easy to Set Up & Customize

🛠️ Technologies Used
Django (Python Backend Framework)

HTML5, CSS3, Bootstrap (Frontend)

SQLite (Default Django Database)

Django Authentication System

📂 Project Structure

mental-health-app/
│── db.sqlite3
│── manage.py
│── requirements.txt
│── assessment/             
│   ├── templates/
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│── project_name/
    ├── settings.py
    ├── urls.py
⚙️ Installation & Setup
1️⃣ Clone the Repository
bash

git clone https://github.com/your-username/mental-health-app.git
cd mental-health-app
2️⃣ Create a Virtual Environment
bash

python -m venv env
Activate it:

Windows

bash

env\Scripts\activate
Mac/Linux

bash

source env/bin/activate
3️⃣ Install Project Dependencies
bash

pip install -r requirements.txt
4️⃣ Apply Migrations
bash

python manage.py migrate
5️⃣ Create Admin/Superuser (Optional)
bash

python manage.py createsuperuser
6️⃣ Run the Server
bash

python manage.py runserver
Open in browser:

👉 http://127.0.0.1:8000/

🧩 How It Works
User creates an account or logs in

User starts the mental health assessment

Answers multiple questions about stress, mood, sleep, emotions, etc.

System calculates results

User receives a mental health status summary

🗄️ Database
This project uses SQLite, Django’s default lightweight database.
Configuration is located in:

bash

project_name/settings.py
python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
No setup required — Django creates this file automatically after migration.



🔗 GitHub Repository
(Add your GitHub link here after upload)

⚠️ Disclaimer
This application is not intended for professional diagnosis.
All assessments are suggestions based on user responses.
For real mental health concerns, always consult a professional.

🤝 Contributing
Contributions, suggestions, and improvements are welcome!