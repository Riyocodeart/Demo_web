# 🛒 Django E-Commerce Backend (Admin Panel)

This Django project provides a simple admin interface to manage **🗂️ Categories**, **📦 Products**, **👤 Customers**, and **🧾 Orders** models for an e-commerce-like system.

---

## 🚀 Features

✅ Admin panel with full CRUD support  
✅ Superuser access for secure model management  
✅ Structured models:
- 🗂️ **Category** – Product grouping (e.g., Electronics, Fashion)
- 📦 **Product** – Item details like name, price, category
- 👤 **Customer** – Customer info (name, contact)
- 🧾 **Order** – Links a customer to a product purchase

---

## 🛠️ Setup Instructions

1. 📁 **Clone the Repository**
   ```bash
   git clone <your-repo-url>
   cd <project-folder>
🐍 Install Dependencies


pip install -r requirements.txt
⚙️ Apply Migrations

python manage.py makemigrations
python manage.py migrate


🔐 Create Superuser

python manage.py createsuperuser
🌐 Start the Development Server

python manage.py runserver
✨ Access the Admin Panel
Go to: http://127.0.0.1:8000/admin
Login with your superuser credentials

📌 Notes
🧠 All models are registered in admin.py for admin use

🛠️ You can expand this project by adding frontend pages or APIs

🔁 Customize the models and admin layout based on your use case

📸 Output:
![image](https://github.com/user-attachments/assets/e862fd97-8acf-4a09-ac77-3b146c838227)
![image](https://github.com/user-attachments/assets/aa25d625-5af1-4d2c-9cb2-e41895c95f6a)


 using Django



