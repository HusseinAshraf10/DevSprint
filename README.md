# DevSprint

Hey! This is a developer collaboration and accountability platform I've been building with Django. It gives developers a space to launch short coding sprints, track bugs, talk through technical stacks, and showcase their completed projects.

I originally started this project following Dennis Ivy's StudyBud tutorial to get hands-on experience with Django fundamentals (MVT architecture, ORM, custom authentication, and database relations). Since finishing the tutorial foundation, I've redesigned the UI with a modern dark theme and transformed it into **DevSprint**—adding developer portfolio passports, sprint verification badges, and REST API endpoints.

---

### What works right now
- **Sprint Management:** Launch, edit, and manage technical sprint rooms with categorized tech stacks.
- **Dev Passport Profiles:** User profiles act as micro-portfolios with real-time stats tracking **Total Sprints**, **Shipped Projects**, and **Contributions**.
- **Project Verification:** Mark sprints as `🏁 Shipped` and link directly to **GitHub Repositories** and **Live Demos**.
- **Live Discussion & Activity Feed:** Real-time room comments, global activity timeline, and participant tracking.
- **Topic Discovery:** Filter sprints by language, framework, or search keywords.
- **REST API:** Built with Django REST Framework (DRF) exposing `/api/rooms/` and individual room endpoints with CORS enabled.
- **Custom Authentication:** Secure registration and login flow using custom email-based authentication.

---

### Tech stack
- **Backend:** Python 3.14, Django 6.1, Django REST Framework (DRF)
- **Database:** SQLite (development) → moving to PostgreSQL
- **Frontend:** Django Templates, Custom CSS (modern dark/obsidian theme), Vanilla JavaScript
- **Libraries:** `django-cors-headers`, `pillow`

---

### How to run it locally

If you'd like to test the project on your machine:

```bash
# 1. Clone the repository
git clone https://github.com/HusseinAshraf10/DevSprint.git
cd DevSprint

# 2. Set up virtual environment
python -m venv env

# Activate it (Windows):
.\env\Scripts\activate
# Or Mac/Linux:
source env/bin/activate

# 3. Install dependencies & migrate
pip install -r requirements.txt
python manage.py migrate

# 4. Start the server
python manage.py runserver
```

Then visit `http://127.0.0.1:8000` in your browser.

---

### What I'm building next
- [ ] **24-Hour Countdown Timer:** Adding automatic sprint expiration and time-boxed challenge clocks.
- [ ] **Automated GitHub Activity Sync:** Pulling latest commit activity directly into sprint check-ins.
- [ ] **PostgreSQL & Production Deployment:** Migrating to PostgreSQL and hosting the app live on Render or Railway.

---

Feedback is always welcome! Feel free to open an issue or connect on [GitHub](https://github.com/HusseinAshraf10).
