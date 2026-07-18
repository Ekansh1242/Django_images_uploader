# Django Image Uploader

A production-ready image upload and gallery web app built with Django 5 and Bootstrap 5.

## Features
- Upload JPG, PNG, JPEG, GIF images (max 10 MB)
- Responsive Bootstrap 5 gallery with lightbox modal view
- File type & size validation (client + server side)
- Delete images with confirmation
- Success/error messaging
- Deployable to Vercel

## Project Structure
```
django_image_uploader/
├── manage.py
├── requirements.txt
├── vercel.json
├── build_files.sh
├── imageuploader/   # Django project settings
├── gallery/         # Main app (models, views, templates, static)
├── media/           # Uploaded images
└── screenshots/     # App screenshots
```

## Local Setup

1. Clone & create a virtual environment
```bash
git clone <repo-url>
cd django_image_uploader
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Create a `.env` file (optional, defaults work for local dev)
```
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

4. Run migrations
```bash
python manage.py migrate
```

5. Create a superuser (optional, for admin access)
```bash
python manage.py createsuperuser
```

6. Run the dev server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/`

## Deployment on Vercel

> Important: Vercel's filesystem is ephemeral and read-only outside `/tmp`. SQLite writes and uploaded media files will NOT persist between deployments/invocations. For real production use, connect a hosted database (e.g. Postgres via `DATABASE_URL`) and cloud storage (e.g. AWS S3 or Cloudinary) for media. The steps below deploy the app as-is for demonstration purposes.

1. Install the Vercel CLI
```bash
npm install -g vercel
```

2. Login
```bash
vercel login
```

3. Add environment variables in the Vercel dashboard (Project → Settings → Environment Variables):
   - SECRET_KEY
   - DEBUG=False
   - ALLOWED_HOSTS=.vercel.app

4. Deploy
```bash
vercel --prod
```

5. Vercel reads `vercel.json`, runs `build_files.sh` (installs deps, collects static, migrates), and routes requests to `imageuploader/wsgi.py`.

6. Once deployed, visit the generated `*.vercel.app` URL.

## Tech Stack
- Django 5.1
- SQLite
- Bootstrap 5 + Bootstrap Icons
- Whitenoise (static file serving)
- Gunicorn (production server)

## License
MIT
