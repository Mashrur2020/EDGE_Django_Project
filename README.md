# ⌚ Watch Store - Django Project  

Welcome to **Watch Store**, a Django-based web application where users can browse and purchase luxury, smart, and classic watches. This project features a well-organized blog layout to display watch collections and their details.  

## 🚀 Features  

✔ **Home Page** - Displays featured watches.  
✔ **Blog Page** - Lists all watches available for purchase with images, descriptions, and prices.  
✔ **Buy Now Button** - Redirects users to external websites for purchasing watches.  
✔ **Admin Panel** - Allows admins to add, update, or delete watch listings.  
✔ **Database Integration** - Uses SQLite to store all watch products.  
✔ **Bootstrap UI** - Provides a responsive and modern layout.  

---

## 🛠️ Installation Guide  

Follow these steps to set up and run the project on your local machine.  

### 1️⃣ **Clone the Repository**  
```bash
git clone https://github.com/yourusername/watch-store.git
cd watch-store


2️⃣ Create a Virtual Environment
python -m venv env
Activate the environment:

Windows: env\Scripts\activate
Mac/Linux: source env/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Create a Superuser (Admin Panel)
python manage.py createsuperuser
Follow the prompts to set up a username and password.
Or use the pre-created credentials below 👇

📌 Admin Panel Login
🔗 URL: http://127.0.0.1:8000/admin/
🆔 Username: admin
🔑 Password: newpassword123

6️⃣ Run the Server
python manage.py runserver
Then open the browser and visit:

Home Page: http://127.0.0.1:8000/
Blog Page: http://127.0.0.1:8000/blog/
Admin Panel: http://127.0.0.1:8000/admin/
📂 Project Structure
bash
Copy
Edit
watch-store/
│── watchstore/   # Django Project Configuration
│── blog/         # Blog App (Models, Views, URLs)
│── templates/    # HTML Templates (base, index, blog)
│── static/       # CSS, JS, and Images
│── db.sqlite3    # Database File
│── manage.py     # Django Management Script
│── env/          # Virtual Environment (Ignore this in Git)
🛠️ Technologies Used
Django (Python Web Framework)
Bootstrap (CSS Framework)
SQLite (Database)
HTML, CSS (Frontend)
🤝 Contributing
Feel free to fork this repository and contribute improvements!

Fork the repository
Create a new branch (git checkout -b feature-branch)
Commit your changes (git commit -m "Added a new feature")
Push to your branch (git push origin feature-branch)
Create a Pull Request
📄 License
This project is open-source and available under the MIT License.
