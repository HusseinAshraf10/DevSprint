# DevSprint

Hey! This is a web app I've been building with Django to create topic-based rooms where developers can share questions, talk through bugs, and do short coding sprints together.

I started this project while following Dennis Ivy's StudyBud tutorial to get comfortable with Django's core concepts (MVT pattern, ORM, authentication, and database relations). Since finishing the basic setup, I've been refactoring the code, redesigning parts of the UI, and turning it into a dedicated sprint and accountability tool.

---

### What works right now
- Create, update, and delete discussion rooms (only the host has permission).
- Filter rooms by topic or search directly by keywords.
- Live room chat and a recent activity feed across the site.
- User profiles with bios, avatars, and a history of rooms and comments.
- Automatic participant tracking when someone posts inside a room.

---

### Tech stack
- **Backend:** Python & Django
- **Database:** SQLite (local dev for now)
- **Frontend:** HTML, CSS, JavaScript (Django templates)

---

### How to run it locally

If you want to clone it and test it out:

```bash
# 1. Clone the repo
git clone https://github.com/HusseinAshraf10/DevSprint.git
cd DevSprint

# 2. Set up virtual environment
python -m venv env

# Activate it (Windows):
.\env\Scripts\activate
# Or Mac/Linux:
source env/bin/activate

# 3. Install packages & migrate
pip install -r requirements.txt
python manage.py migrate

# 4. Start the server
python manage.py runserver
```

Then just visit `http://127.0.0.1:8000` in your browser.

---

### What I'm working on next
- Adding a 24-hour sprint countdown timer for rooms.
- Allowing users to share links to their GitHub pull requests or live demos.
- Moving from SQLite to PostgreSQL and deploying it live.

---

Feedback is always welcome! Feel free to open an issue or reach out.
