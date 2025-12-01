# GitHub & Render Deployment Guide

## Project Structure Overview

Your project is well-structured for deployment. Here's what's included:

```
Haramaya-University-Health-Center/
├── appointments/          # Appointments management app
├── billing/              # Billing system app
├── core/                 # Core app with custom User model
├── doctors/              # Doctors management app
├── laboratory/           # Laboratory tests app
├── patients/             # Patients management app
├── pharmacy/             # Pharmacy management app
├── hospital_system/      # Main Django project settings
├── templates/            # HTML templates
├── ml_models/            # Machine learning models
├── datasets/             # Data files
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
├── runtime.txt           # Python version (3.11.0)
├── Procfile              # Heroku/Render process file
├── render.yaml           # Render deployment config
├── build.sh              # Build script for Render
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
└── README.md             # Project documentation
```

## Pre-Deployment Checklist

### 1. Clean Up Before Pushing to GitHub

Remove these files/folders from git (they're already in .gitignore):
- `db.sqlite3` - Local database
- `*.pyc` - Python compiled files
- `__pycache__/` - Python cache
- `.venv/` or `venv/` - Virtual environment
- `staticfiles/` - Collected static files
- `.env` - Environment variables (use .env.example instead)
- `set_password.py` - Temporary script (optional)

### 2. Verify .gitignore

Your `.gitignore` already covers:
- Python cache files
- Virtual environments
- Database files
- Static files
- Environment variables
- IDE files

### 3. Update .env.example

Current `.env.example` includes all necessary variables. Ensure it has:
```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,.onrender.com
DATABASE_URL=postgresql://user:password@host:port/dbname
```

## Step 1: Prepare for GitHub

### 1.1 Initialize Git (if not already done)
```bash
git init
git add .
git commit -m "Initial commit: Hospital Management System"
```

### 1.2 Create .env file (local only, not committed)
```bash
cp .env.example .env
# Edit .env with your local settings
```

### 1.3 Verify files to exclude
```bash
git status
# Should NOT show: db.sqlite3, .env, __pycache__, venv/
```

## Step 2: Push to GitHub

### 2.1 Create GitHub Repository
1. Go to https://github.com/new
2. Create repository: `hospital-management-system`
3. Do NOT initialize with README (you have one)

### 2.2 Push Code
```bash
git remote add origin https://github.com/YOUR_USERNAME/hospital-management-system.git
git branch -M main
git push -u origin main
```

## Step 3: Deploy on Render

### 3.1 Create Render Account
1. Go to https://render.com
2. Sign up with GitHub account
3. Connect your GitHub account

### 3.2 Create Web Service
1. Click "New +" → "Web Service"
2. Select your GitHub repository
3. Configure:
   - **Name:** `hospital-management-system`
   - **Environment:** `Python 3`
   - **Build Command:** `./build.sh`
   - **Start Command:** `gunicorn hospital_system.wsgi:application`
   - **Plan:** Free (or paid if needed)

### 3.3 Add Environment Variables
In Render dashboard, add these environment variables:

```
DEBUG=False
SECRET_KEY=<generate-a-strong-key>
ALLOWED_HOSTS=.onrender.com
DATABASE_URL=<will-be-auto-set-if-using-Render-DB>
PYTHON_VERSION=3.11.0
```

### 3.4 Create PostgreSQL Database (Optional but Recommended)
1. Click "New +" → "PostgreSQL"
2. Configure:
   - **Name:** `hospital-db`
   - **Database:** `hospital_db`
   - **User:** `hospital_user`
   - **Plan:** Free
3. Render will auto-populate `DATABASE_URL`

### 3.5 Deploy
1. Click "Create Web Service"
2. Render will automatically deploy from your GitHub repo
3. Monitor deployment in the "Logs" tab

## Step 4: Post-Deployment

### 4.1 Create Superuser on Render
```bash
# In Render dashboard, go to your service
# Click "Shell" tab
# Run:
python manage.py createsuperuser
```

### 4.2 Load Sample Data (Optional)
```bash
python manage.py load_sample_data
```

### 4.3 Verify Deployment
- Visit: `https://your-service-name.onrender.com`
- Admin panel: `https://your-service-name.onrender.com/admin/`

## Important Notes

### Database
- **Local:** SQLite (db.sqlite3)
- **Render:** PostgreSQL (recommended for production)
- Migrations run automatically via `build.sh`

### Static Files
- Collected automatically during build
- Served by WhiteNoise middleware
- No separate static file service needed

### Media Files
- Uploaded files stored in `/media/`
- On Render free tier, files are ephemeral
- Consider using cloud storage (AWS S3, Cloudinary) for production

### Environment Variables
- Never commit `.env` file
- Always use `.env.example` as template
- Render auto-generates `SECRET_KEY` if not provided

### Monitoring
- Check Render logs for errors
- Monitor database usage
- Set up alerts for failures

## Troubleshooting

### Build Fails
1. Check build logs in Render dashboard
2. Verify `build.sh` is executable: `chmod +x build.sh`
3. Ensure all dependencies in `requirements.txt`

### Database Connection Error
1. Verify `DATABASE_URL` is set correctly
2. Check PostgreSQL service is running
3. Run migrations: `python manage.py migrate`

### Static Files Not Loading
1. Verify `STATIC_ROOT` and `STATIC_URL` in settings
2. Run: `python manage.py collectstatic --noinput`
3. Check WhiteNoise middleware is installed

### Admin Panel Not Accessible
1. Create superuser: `python manage.py createsuperuser`
2. Verify `LOGIN_URL` and `LOGIN_REDIRECT_URL` in settings

## Security Checklist

- [ ] `DEBUG=False` in production
- [ ] Strong `SECRET_KEY` generated
- [ ] `ALLOWED_HOSTS` configured correctly
- [ ] HTTPS enforced (Render does this automatically)
- [ ] Database credentials in environment variables
- [ ] `.env` file in `.gitignore`
- [ ] CORS settings configured for your domain
- [ ] CSRF trusted origins updated

## Next Steps

1. Clean up local files
2. Push to GitHub
3. Connect Render to GitHub
4. Deploy and test
5. Monitor logs and performance
6. Set up custom domain (optional)
7. Configure email service (optional)
8. Set up backups (optional)

---

**Your project is ready for deployment!** All necessary files are in place.
