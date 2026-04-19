# 🚀 Django Portfolio Website

A full-stack portfolio website built using Django, featuring dynamic project pages, a contact system with real-time email notifications, and cloud deployment on Render.

🌐 **[Live Demo](https://portfolio-c9ce.onrender.com)**

---

## 📸 Screenshots

> Add screenshots here:
> - Home page with hero section
> - Projects showcase
> - Contact form
> - Mobile responsive design

---

## ✨ Features

- **Home Page** - Responsive landing section with modern UI and smooth scrolling
- **Projects Showcase** - Dynamic project pages with detailed descriptions (SoilGuard, Finance)
- **About Section** - Professional bio and skills overview
- **Experience Timeline** - Chronological work experience display
- **Testimonials** - Client/colleague feedback section
- **Contact Form** - Backend-integrated form with email notifications via SMTP
- **Email Notifications** - Automatic emails sent to your Gmail inbox when someone submits the form
- **Auto-reply** - Automatic thank you email response to contacts
- **Admin Panel** - Django admin dashboard for managing content

---

## 🧠 Skills Demonstrated

- **Full-stack web development** with Django framework
- **Backend architecture** with REST-style request handling
- **Email integration** via SMTP (Gmail)
- **Cloud deployment & hosting** (Render.com)
- **Database design & modeling** with SQLite
- **Frontend development** with HTML, CSS
- **Security best practices** (environment variables, app passwords)
- **Version control** with Git & GitHub
- **MVC architecture** implementation

---

## 🛠️ Tech Stack

- **Backend**: Django 4.2 (Python)
- **Database**: SQLite
- **Frontend**: HTML5, CSS3
- **Email Service**: Gmail SMTP
- **Hosting**: Render.com
- **Version Control**: Git & GitHub

---

## 📋 Quick Start

### Local Development

#### 1. Clone & Setup
```bash
git clone https://github.com/saisanket232/portfolio.git
cd portfolio
python -m venv venv
venv\Scripts\activate
pip install -r portfolio_project/requirements.txt
```

#### 2. Configure Gmail
1. Go to [Google Account Security](https://myaccount.google.com/security)
2. Enable 2-Step Verification
3. Generate App Password (Mail → Other)
4. Set environment variables:

```powershell
$env:EMAIL_HOST_USER = 'yourgmail@gmail.com'
$env:EMAIL_HOST_PASSWORD = 'your_16_char_app_password'
```

#### 3. Run Locally
```bash
cd portfolio_project
python manage.py migrate
python manage.py runserver
```

Visit: `http://localhost:8000`

---

## 🚀 Deployment on Render


### 1. Push to GitHub
```bash
git add .
git commit -m "Initial portfolio setup"
git push
```

### 2. Deploy on Render

1. Go to [render.com](https://render.com) and sign in with GitHub
2. Click **New** → **Web Service**
3. Connect your portfolio repository
4. Configure:
   - **Name**: portfolio
   - **Runtime**: Python 3.11
   - **Build Command**: `pip install -r portfolio_project/requirements.txt`
   - **Start Command**: `cd portfolio_project && gunicorn portfolio_project.wsgi:application`

### 3. Add Environment Variables

In Render dashboard → **Environment**:

```
EMAIL_HOST_USER=yourgmail@gmail.com
EMAIL_HOST_PASSWORD=your_16_char_app_password
```

---

## 🔐 Security Architecture

**Email Configuration** (`settings.py`)
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
```

**Key Security Practices:**
- ✅ Credentials stored in environment variables only
- ✅ Gmail App Passwords (more secure than account password)
- ✅ CSRF protection enabled
- ✅ DEBUG = False in production
- ✅ No hardcoded secrets in repository

---

## 📁 Project Structure

```
portfolio_project/
├── portfolio/
│   ├── migrations/
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── about.html
│   │   ├── projects.html
│   │   ├── experience.html
│   │   ├── testimonials.html
│   │   ├── contact.html
│   │   └── projects/
│   │       ├── soilguard.html
│   │       └── finance.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── portfolio_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── manage.py
```

---

## 📧 Contact Form Workflow

```
User submits form
    ↓
Data saved to database (ContactMessage)
    ↓
Email sent to your Gmail inbox
    ↓
Auto-reply sent to contact
    ↓
Success message displayed to user
```

**Backend Implementation** (`views.py`)
```python
def contact(request):
    if request.method == "POST":
        # Save to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )
        
        # Send email notification
        send_mail(...)
        
        # Send auto-reply
        send_mail(...)
        
        return render(request, "contact.html", {"success": "Message sent!"})
```


---

## 📊 Performance Tips

- Static files are served via WhiteNoise middleware
- Email sending is synchronous (consider Celery for async in production)
- SQLite is fine for small projects; upgrade to PostgreSQL for scaling

---

## 🚀 Future Enhancements

- [ ] Add success popup notification
- [ ] Add reCAPTCHA spam protection
- [ ] Add loading animation on form submit
- [ ] Upgrade to PostgreSQL database
- [ ] Add custom domain (saisanket.dev)
- [ ] Add API endpoints
- [ ] Implement search functionality
- [ ] Add dark mode toggle

---

## 📄 License

This project is open source and available for personal use.

---

## 👤 Author

**Sai Sanket M**  
[Portfolio](https://portfolio-c9ce.onrender.com)

Made with ❤️ using Django 
