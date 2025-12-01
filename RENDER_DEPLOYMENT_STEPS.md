# 🚀 Step-by-Step Guide to Deploy on Render

## Complete Deployment Instructions for Haramaya University Health Center

**Estimated Time:** 20-30 minutes  
**Difficulty:** Easy  
**Prerequisites:** GitHub account, Render account

---

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Step 1: Create Render Account](#step-1-create-render-account)
3. [Step 2: Connect GitHub](#step-2-connect-github)
4. [Step 3: Create Web Service](#step-3-create-web-service)
5. [Step 4: Configure Environment Variables](#step-4-configure-environment-variables)
6. [Step 5: Create PostgreSQL Database](#step-5-create-postgresql-database)
7. [Step 6: Deploy](#step-6-deploy)
8. [Step 7: Post-Deployment Setup](#step-7-post-deployment-setup)
9. [Step 8: Verify Deployment](#step-8-verify-deployment)
10. [Troubleshooting](#troubleshooting)

---

## Prerequisites

Before you start, make sure you have:

- ✅ GitHub account with repository pushed
- ✅ Render account (free)
- ✅ Internet connection
- ✅ Web browser

### Repository URL
```
https://github.com/charidedecha7-ops/Haramaya-University-Health-Center.git
```

---

## Step 1: Create Render Account

### 1.1 Go to Render Website
1. Open browser and go to: **https://render.com**
2. Click **"Sign Up"** button (top right)

### 1.2 Sign Up with GitHub
1. Click **"Continue with GitHub"**
2. You'll be redirected to GitHub login
3. Enter your GitHub credentials
4. Click **"Authorize render"**
5. Complete the Render signup form
6. Click **"Create Account"**

### 1.3 Verify Email
1. Check your email for Render verification
2. Click the verification link
3. Your account is now active

**✅ Step 1 Complete**

---

## Step 2: Connect GitHub

### 2.1 Connect GitHub Repository
1. Go to Render Dashboard: https://dashboard.render.com
2. Click **"New +"** button (top right)
3. Select **"Web Service"**
4. Click **"Connect a repository"**

### 2.2 Select Repository
1. Search for: **"Haramaya-University-Health-Center"**
2. Click **"Connect"** next to your repository
3. You may need to authorize Render to access GitHub

### 2.3 Grant Permissions
1. If prompted, click **"Authorize render"**
2. Select your repository
3. Click **"Install"**

**✅ Step 2 Complete**

---

## Step 3: Create Web Service

### 3.1 Configure Web Service
After connecting repository, fill in the form:

**Name:**
```
hospital-management-system
```

**Environment:**
```
Python 3
```

**Region:**
```
Choose closest to you (e.g., us-east-1)
```

**Branch:**
```
main
```

**Build Command:**
```
./build.sh
```

**Start Command:**
```
gunicorn hospital_system.wsgi:application
```

### 3.2 Select Plan
- **Plan:** Free (or Starter if you want better performance)
- Click **"Create Web Service"**

**Note:** Free plan is sufficient for testing. Render will start building.

**✅ Step 3 Complete**

---

## Step 4: Configure Environment Variables

### 4.1 Add Environment Variables
1. In Render dashboard, go to your service
2. Click **"Environment"** tab (left sidebar)
3. Click **"Add Environment Variable"**

### 4.2 Add Each Variable

**Variable 1: DEBUG**
```
Key: DEBUG
Value: False
```
Click **"Add"**

**Variable 2: SECRET_KEY**
```
Key: SECRET_KEY
Value: django-insecure-your-secret-key-here-change-this-in-production
```
Click **"Add"**

**Variable 3: ALLOWED_HOSTS**
```
Key: ALLOWED_HOSTS
Value: .onrender.com
```
Click **"Add"**

**Variable 4: PYTHON_VERSION**
```
Key: PYTHON_VERSION
Value: 3.11.0
```
Click **"Add"**

### 4.3 Generate Strong SECRET_KEY (Optional)
If you want a stronger SECRET_KEY:
1. Go to: https://djecrety.ir/
2. Click **"Generate"**
3. Copy the generated key
4. Paste it in the SECRET_KEY value

**✅ Step 4 Complete**

---

## Step 5: Create PostgreSQL Database

### 5.1 Create Database Service
1. Go to Render Dashboard
2. Click **"New +"** button
3. Select **"PostgreSQL"**

### 5.2 Configure Database
**Name:**
```
hospital-db
```

**Database:**
```
hospital_db
```

**User:**
```
hospital_user
```

**Region:**
```
Same as web service
```

**Plan:**
```
Free
```

### 5.3 Create Database
1. Click **"Create Database"**
2. Wait for database to be created (2-3 minutes)
3. Copy the **Internal Database URL**

### 5.4 Add DATABASE_URL to Web Service
1. Go back to your web service
2. Click **"Environment"** tab
3. Click **"Add Environment Variable"**

**Variable: DATABASE_URL**
```
Key: DATABASE_URL
Value: [Paste the Internal Database URL from PostgreSQL]
```

Click **"Add"**

**✅ Step 5 Complete**

---

## Step 6: Deploy

### 6.1 Trigger Deployment
1. Go to your web service
2. Click **"Manual Deploy"** button (top right)
3. Select **"Deploy latest commit"**
4. Render will start building and deploying

### 6.2 Monitor Deployment
1. Click **"Logs"** tab to see build progress
2. Watch for messages like:
   - "Building..."
   - "Running migrations..."
   - "Collecting static files..."
   - "Starting server..."

### 6.3 Wait for Completion
- Deployment typically takes 5-10 minutes
- You'll see: **"Your service is live"** when complete
- The URL will be displayed at the top

**Example URL:**
```
https://hospital-management-system.onrender.com
```

**✅ Step 6 Complete**

---

## Step 7: Post-Deployment Setup

### 7.1 Create Superuser
1. Go to your service in Render
2. Click **"Shell"** tab
3. Run this command:
```bash
python manage.py createsuperuser
```

4. Enter details:
   - **Username:** admin
   - **Email:** admin@hospital.com
   - **Password:** (create a strong password)
   - **Confirm Password:** (repeat password)

### 7.2 Load Sample Data (Optional)
In the Shell, run:
```bash
python manage.py load_sample_data
```

This will load:
- 5 Doctors
- 6 Patients
- 10 Medicines
- 5 Lab Tests
- 5 Appointments
- 3 Bills

### 7.3 Exit Shell
Type: `exit` and press Enter

**✅ Step 7 Complete**

---

## Step 8: Verify Deployment

### 8.1 Access Your Application
1. Go to your service URL (shown in Render dashboard)
2. Example: `https://hospital-management-system.onrender.com`

### 8.2 Test Main Pages
- **Main Page:** https://your-url.onrender.com
- **Demo Page:** https://your-url.onrender.com/demo/
- **Admin Panel:** https://your-url.onrender.com/admin/

### 8.3 Login and Test
1. Go to Admin: https://your-url.onrender.com/admin/
2. Login with credentials you created
3. Verify all modules are working:
   - Patients
   - Doctors
   - Appointments
   - Laboratory
   - Pharmacy
   - Billing

### 8.4 View Sample Data
1. Go to Demo Page: https://your-url.onrender.com/demo/
2. Verify all sample data is displayed:
   - 5 Doctors
   - 6 Patients
   - 10 Medicines
   - 5 Lab Tests
   - 5 Appointments
   - 3 Bills

**✅ Step 8 Complete**

---

## Troubleshooting

### Issue 1: Build Failed

**Error:** "Build failed"

**Solution:**
1. Check the Logs tab for error messages
2. Common causes:
   - Missing environment variables
   - Python version mismatch
   - Dependency issues

**Fix:**
1. Verify all environment variables are set
2. Check `requirements.txt` is correct
3. Check `runtime.txt` has Python 3.11.0
4. Click "Manual Deploy" to retry

### Issue 2: Database Connection Error

**Error:** "Could not connect to database"

**Solution:**
1. Verify DATABASE_URL is set correctly
2. Check PostgreSQL database is running
3. Verify database credentials

**Fix:**
1. Go to Environment variables
2. Check DATABASE_URL value
3. Make sure it starts with `postgresql://`
4. Redeploy

### Issue 3: Static Files Not Loading

**Error:** CSS/images not displaying

**Solution:**
1. Static files should be collected automatically
2. Check build logs for "Collecting static files"

**Fix:**
1. In Shell, run: `python manage.py collectstatic --noinput`
2. Redeploy

### Issue 4: Admin Panel Not Accessible

**Error:** "Page not found" at /admin/

**Solution:**
1. Verify superuser was created
2. Check migrations were applied

**Fix:**
1. In Shell, run: `python manage.py migrate`
2. Create superuser again if needed
3. Redeploy

### Issue 5: Sample Data Not Showing

**Error:** Demo page shows no data

**Solution:**
1. Sample data needs to be loaded
2. Check if load_sample_data command ran

**Fix:**
1. In Shell, run: `python manage.py load_sample_data`
2. Refresh the demo page

### Issue 6: Service Keeps Crashing

**Error:** "Service crashed" or "503 Service Unavailable"

**Solution:**
1. Check logs for error messages
2. Common causes:
   - Missing environment variables
   - Database connection issues
   - Code errors

**Fix:**
1. Check all environment variables are set
2. Verify DATABASE_URL is correct
3. Check application logs
4. Redeploy

---

## Quick Reference

### Important URLs
```
Dashboard: https://dashboard.render.com
Your App: https://hospital-management-system.onrender.com
Admin: https://hospital-management-system.onrender.com/admin/
Demo: https://hospital-management-system.onrender.com/demo/
```

### Important Commands (in Shell)
```bash
# Create superuser
python manage.py createsuperuser

# Load sample data
python manage.py load_sample_data

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Check database
python manage.py dbshell
```

### Environment Variables
```
DEBUG=False
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=.onrender.com
PYTHON_VERSION=3.11.0
DATABASE_URL=postgresql://...
```

---

## Post-Deployment Checklist

- [ ] Render account created
- [ ] GitHub connected
- [ ] Web service created
- [ ] Environment variables added
- [ ] PostgreSQL database created
- [ ] DATABASE_URL added
- [ ] Deployment completed
- [ ] Superuser created
- [ ] Sample data loaded
- [ ] Main page accessible
- [ ] Admin panel working
- [ ] Demo page showing data
- [ ] All modules tested

---

## Performance Tips

### Optimize Your Deployment

1. **Use PostgreSQL** (not SQLite)
   - Better performance
   - Supports concurrent users
   - More reliable

2. **Enable Caching**
   - Reduces database queries
   - Faster page loads

3. **Optimize Images**
   - Compress images
   - Use appropriate formats

4. **Monitor Performance**
   - Check Render metrics
   - Monitor database usage
   - Track response times

5. **Set Up Backups**
   - Regular database backups
   - Automated backups recommended

---

## Security Checklist

- [ ] DEBUG set to False
- [ ] SECRET_KEY is strong and unique
- [ ] ALLOWED_HOSTS configured correctly
- [ ] Database credentials in environment variables
- [ ] HTTPS enforced (automatic on Render)
- [ ] CSRF protection enabled
- [ ] Password validators configured
- [ ] Audit logging enabled
- [ ] Regular backups configured
- [ ] Monitoring set up

---

## Next Steps After Deployment

### Immediate
1. Test all features
2. Verify sample data
3. Check admin panel
4. Test user logins

### Short-term
1. Create additional users
2. Add real data
3. Configure email service
4. Set up custom domain (optional)

### Long-term
1. Monitor performance
2. Collect user feedback
3. Plan feature enhancements
4. Set up automated backups
5. Configure monitoring and alerts

---

## Support & Resources

### Render Documentation
- https://render.com/docs
- https://render.com/docs/deploy-django

### Django Documentation
- https://docs.djangoproject.com/
- https://www.django-rest-framework.org/

### PostgreSQL Documentation
- https://www.postgresql.org/docs/

### Troubleshooting
- Check Render logs
- Review Django error messages
- Check database connection
- Verify environment variables

---

## Estimated Timeline

| Step | Time | Status |
|------|------|--------|
| Create Render Account | 5 min | ⏳ |
| Connect GitHub | 2 min | ⏳ |
| Create Web Service | 5 min | ⏳ |
| Configure Environment | 5 min | ⏳ |
| Create Database | 3 min | ⏳ |
| Deploy | 5-10 min | ⏳ |
| Post-Deployment Setup | 5 min | ⏳ |
| Verify | 5 min | ⏳ |
| **Total** | **30-40 min** | ⏳ |

---

## Success Indicators

✅ **Deployment Successful When:**
- Service shows "Live" status
- URL is accessible
- Admin panel loads
- Demo page shows data
- All modules working
- No error messages

---

## Common Questions

### Q: Can I use the free plan?
**A:** Yes! Free plan is perfect for testing and small deployments.

### Q: How long does deployment take?
**A:** Usually 5-10 minutes after you click deploy.

### Q: Can I use SQLite instead of PostgreSQL?
**A:** Not recommended. PostgreSQL is better for production.

### Q: How do I update my code?
**A:** Push changes to GitHub, then click "Manual Deploy" in Render.

### Q: Can I set a custom domain?
**A:** Yes! Go to Settings → Custom Domain in Render.

### Q: How do I backup my database?
**A:** Render provides automated backups. Check Settings → Backups.

---

## Final Notes

- Your application is now live on the internet
- Anyone can access it via the URL
- Keep your SECRET_KEY secure
- Monitor your usage and costs
- Set up alerts for errors
- Regular backups are recommended

---

**Congratulations! Your system is now deployed on Render! 🎉**

**Your Application URL:** https://hospital-management-system.onrender.com

**Admin Panel:** https://hospital-management-system.onrender.com/admin/

**Demo Page:** https://hospital-management-system.onrender.com/demo/

---

**Need Help?**
- Check Render documentation: https://render.com/docs
- Review Django docs: https://docs.djangoproject.com/
- Check application logs in Render dashboard

**Happy Deploying! 🚀**
