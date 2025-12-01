# Haramaya University Health Center - Quick Start Guide

## 🚀 Getting Started

### System is Running
Your Django development server is already running at: **http://127.0.0.1:8000**

---

## 🔐 Login Credentials

### Admin Account
```
Username: admin
Password: admin123
URL: http://127.0.0.1:8000/admin/
```

### Doctor Accounts (Choose Any)
```
Username: dr_abebe    | Password: doctor123
Username: dr_tigist   | Password: doctor123
Username: dr_dawit    | Password: doctor123
Username: dr_almaz    | Password: doctor123
Username: dr_hanna    | Password: doctor123
```

---

## 📊 Sample Data Loaded

✅ **5 Doctors** with different specializations
✅ **6 Patients** with complete medical records
✅ **18 Medicines** in pharmacy inventory
✅ **13 Laboratory Tests** with results
✅ **18 Appointments** scheduled
✅ **5 Bills** with payment tracking

---

## 🎨 Logo Integration

The Haramaya University logo has been integrated:
- **Location:** `static/images/haramaya-logo.svg`
- **Display:** Dashboard welcome banner & navigation bar
- **Colors:** Green (university), Orange (accent), Blue (border)

---

## 📱 Main Features to Explore

### 1. **Dashboard** (Home)
- Overview of system statistics
- Quick access to main functions
- Role-based information display

### 2. **Patients Management**
- View all patients
- Register new patients
- Update patient information
- View medical history

### 3. **Doctors Management**
- View doctor profiles
- Check specializations
- View availability
- Manage consultation fees

### 4. **Appointments**
- Schedule new appointments
- View appointment calendar
- Update appointment status
- Track appointment history

### 5. **Laboratory**
- Request lab tests
- View test results
- Track pending tests
- Generate lab reports

### 6. **Pharmacy**
- View medicine inventory
- Check medicine availability
- Create prescriptions
- Track medicine stock

### 7. **Billing**
- Create bills
- Track payments
- View billing history
- Generate invoices

---

## 🔍 Testing Scenarios

### Scenario 1: Doctor Checking Appointments
1. Login as `dr_abebe` / `doctor123`
2. Go to Dashboard
3. View "My Today's Appointments"
4. Click on appointment to see patient details

### Scenario 2: Registering a New Patient
1. Login as admin
2. Go to Patients → Add Patient
3. Fill in patient information
4. Save and view patient profile

### Scenario 3: Scheduling an Appointment
1. Login as admin
2. Go to Appointments → New Appointment
3. Select patient and doctor
4. Choose date and time
5. Add reason and notes
6. Save appointment

### Scenario 4: Creating a Lab Test
1. Login as admin
2. Go to Laboratory → New Test
3. Select patient
4. Choose test type
5. Assign to doctor
6. Save test

### Scenario 5: Managing Pharmacy
1. Login as admin
2. Go to Pharmacy → Medicines
3. View inventory
4. Check stock levels
5. Create prescription if needed

### Scenario 6: Billing Process
1. Login as admin
2. Go to Billing → Bills
3. Create new bill for patient
4. Add services/items
5. Record payment
6. Generate invoice

---

## 📊 Admin Panel Features

Access admin panel at: **http://127.0.0.1:8000/admin/**

### Available Models
- Users (with roles)
- Doctors
- Patients
- Appointments
- Laboratory Tests
- Medicines
- Prescriptions
- Bills
- Audit Logs

### Admin Actions
- Create, Read, Update, Delete records
- Filter and search
- Bulk actions
- Export data
- View audit logs

---

## 🛠️ Useful Commands

### Reload Sample Data
```bash
python Haramaya-University-Health-Center/setup_logo_and_data.py
```

### Create New Superuser
```bash
python manage.py createsuperuser
```

### Run Migrations
```bash
python manage.py migrate
```

### Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### Access Django Shell
```bash
python manage.py shell
```

---

## 📈 System Statistics

### Current Data
- **Total Users:** 12 (1 admin + 5 doctors + 6 patients)
- **Total Appointments:** 18
- **Total Lab Tests:** 13
- **Total Medicines:** 18
- **Total Bills:** 5

### Revenue Tracking
- **Consultation Fees:** 150-300 ETB per doctor
- **Lab Tests:** 40-150 ETB per test
- **Total Billing:** 5,750 ETB
- **Paid Amount:** 3,500 ETB
- **Outstanding:** 2,250 ETB

---

## 🌐 API Endpoints (REST)

The system includes REST API endpoints:

```
/api/patients/
/api/doctors/
/api/appointments/
/api/laboratory/
/api/pharmacy/
/api/billing/
```

### Example API Call
```bash
curl -H "Authorization: Bearer TOKEN" http://127.0.0.1:8000/api/patients/
```

---

## 🔒 Security Features

✅ User authentication and authorization
✅ Role-based access control
✅ Password hashing
✅ CSRF protection
✅ SQL injection prevention
✅ Audit logging
✅ Session management

---

## 📱 Responsive Design

The system is fully responsive:
- ✅ Desktop (1920px+)
- ✅ Tablet (768px - 1024px)
- ✅ Mobile (320px - 767px)

---

## 🐛 Troubleshooting

### Issue: Logo not displaying
**Solution:** Run `python manage.py collectstatic --noinput`

### Issue: Database errors
**Solution:** Run `python manage.py migrate`

### Issue: Static files not loading
**Solution:** Check `STATIC_ROOT` and `STATIC_URL` in settings

### Issue: Can't login
**Solution:** Verify username/password and check user role

---

## 📞 Support Information

### System Components
- **Framework:** Django 4.2
- **Database:** SQLite (local) / PostgreSQL (production)
- **Frontend:** Bootstrap 5
- **API:** Django REST Framework
- **Authentication:** Django built-in

### Key Files
- Settings: `hospital_system/settings.py`
- URLs: `hospital_system/urls.py`
- Database: `db.sqlite3`
- Static Files: `static/`
- Templates: `templates/`

---

## 🚀 Next Steps

1. **Explore the System**
   - Login and navigate through all modules
   - Test different user roles
   - Create and modify records

2. **Customize**
   - Update templates with your branding
   - Modify colors and styling
   - Add custom fields

3. **Deploy**
   - Follow deployment guide
   - Set up production database
   - Configure environment variables

4. **Extend**
   - Add new features
   - Integrate with external services
   - Create custom reports

---

## 📚 Documentation

- **Deployment Guide:** `GITHUB_RENDER_DEPLOYMENT.md`
- **Sample Data:** `SAMPLE_DATA_SUMMARY.md`
- **Deployment Readiness:** `DEPLOYMENT_READINESS_SUMMARY.md`
- **Logo Integration:** `Haramaya-University-Health-Center/LOGO_INTEGRATION.md`

---

## ✅ Checklist

- [x] System running at http://127.0.0.1:8000
- [x] Admin account created (admin/admin123)
- [x] Sample data loaded (5 doctors, 6 patients, etc.)
- [x] Logo integrated and displaying
- [x] Database migrations applied
- [x] Static files collected
- [x] All modules functional
- [x] Ready for testing and deployment

---

**Happy Testing! 🎉**

For questions or issues, refer to the documentation files or check the Django/DRF documentation.

---

**Last Updated:** December 1, 2025  
**System Status:** ✅ Fully Operational
