# 📚 StudyBud

It is a Django-based web application that lets users create topics, rooms, and join study rooms, share messages, and collaborate in real time.  

---

## 🚀 Features

- **User Authentication**
  - Sign up, log in, log out
  - Update profile information and avatar
- **Study Rooms**
  - Create, update, and delete rooms
  - Join rooms and participate in discussions
- **Real-time Discussions**
  - Post and reply to messages inside rooms
- **Search & Filter**
  - Find rooms by topic or name
- **Activity Feed**
  - See recent messages and interactions
- **Responsive Design**
  - Works on desktop, tablet, and mobile

---

## 🛠 Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite 
- **Other Tools:** Django ORM, Django Authentication System

---

## 📦 Installation & Setup

1. **Clone the repository**
   ```
   git clone https://github.com/<your-username>/studybud.git
   cd studybud

   ```
2. Create and activate a virtual environment
   ```
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
   ```
3. Install dependencies
   ```
   pip install -r requirements.txt
   ```
4. Run migrations
   ```
   python manage.py migrate
   ```
5. Create a superuser
   ```
   python manage.py createsuperuser
   ```
6. Run the development server
   ```
   python manage.py runserver
   ```
   

