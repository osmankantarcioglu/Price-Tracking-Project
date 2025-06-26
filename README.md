# Deploying to Render

1. Push your code to GitHub.
2. Go to [Render.com](https://render.com/) and create a new Web Service.
3. Connect your GitHub repo.
4. Set the following environment variables in the Render dashboard:
   - `SECRET_KEY` (your Django secret key)
   - `DEBUG` (set to `False`)
   - `ALLOWED_HOSTS` (e.g., your-app.onrender.com)
   - `DATABASE_URL` (provided by Render PostgreSQL add-on)
   - Any email settings you want
5. Use these commands:
   - **Build Command:**
     ```
     pip install -r requirements.txt
     python manage.py collectstatic --noinput
     python manage.py migrate
     ```
   - **Start Command:**
     ```
     gunicorn cruisetracker.wsgi
     ```
6. Visit your Render URL to see your deployed app! 