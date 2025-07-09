# 🛒 Django E-Commerce Backend (Admin Panel)

This Django project provides a simple admin interface to manage **🗂️ Categories**, **📦 Products**, **👤 Customers**, and **🧾 Orders** models for an e-commerce-like system.
![image](https://github.com/user-attachments/assets/b3b6a7fe-9623-4518-b7a3-83178a9c55c8)
<br><br>
![image](https://github.com/user-attachments/assets/bc818540-ea6c-4170-9333-4b72b92671c5)


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
 using Django

📸 Output:
![image](https://github.com/user-attachments/assets/e862fd97-8acf-4a09-ac77-3b146c838227)


![image](https://github.com/user-attachments/assets/6980b4cc-a9c1-42e4-8ce0-4a448476ff2e)


![image](https://github.com/user-attachments/assets/c6227984-21cd-4e82-a279-dcd6869550c3)





