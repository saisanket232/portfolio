# Portfolio Website

A professional portfolio website built with Django. Features projects, experience, testimonials, and a working contact form with email notifications.

## 🚀 Features

- **Home Page** - Eye-catching landing page
- **About Section** - Professional bio
- **Projects Showcase** - Display your projects (SoilGuard, Finance)
- **Experience Timeline** - Show your work experience
- **Testimonials** - Client/colleague feedback
- **Contact Form** - Fully functional contact form with Gmail integration
- **Email Notifications** - Automatic emails to your Gmail inbox when someone submits the form
- **Auto-reply** - Automatic thank you email to the contact

## 🛠️ Tech Stack

- **Backend**: Django 4.2
- **Database**: SQLite
- **Frontend**: HTML/CSS
- **Email**: Gmail SMTP
- **Hosting**: Render.com

## 📋 Setup Instructions

### 1. Local Development

#### Clone the repository
```bash
git clone https://github.com/saisanket232/portfolio.git
cd portfolio
```

#### Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

#### Install dependencies
```bash
pip install -r requirements.txt
```

#### Run migrations
```bash
cd portfolio_project
python manage.py migrate
```

#### Set up Gmail credentials

Get your Gmail App Password:
1. Go to [Google Account Security](https://myaccount.google.com/security)
2. Enable 2-Step Verification (if not done)
3. Search for "App Passwords"
4. Select Mail → Other
5. Copy the 16-character password

Set environment variables (PowerShell):
```powershell
$env:EMAIL_HOST_USER = 'yourgmail@gmail.com'
$env:EMAIL_HOST_PASSWORD = 'your_app_password_here'
```

#### Run the server
```bash
python manage.py runserver
```

Visit: `http://localhost:8000`

### 2. Email Configuration

The email settings use environment variables for security:

```python
# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
```

**Never hardcode credentials in the code!**

### 3. Deployment on Render

#### Push to GitHub
```bash
git add .
git commit -m "your message"
git push
```

#### Create Render deployment

1. Go to [render.com](https://render.com)
2. Connect your GitHub repository
3. Create Web Service
4. Set environment variables:
   - `EMAIL_HOST_USER` = your Gmail address
   - `EMAIL_HOST_PASSWORD` = your Gmail App Password

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

## 📧 Contact Form Flow

1. User fills out contact form on `/contact`
2. Data is saved to database (`ContactMessage` model)
3. Email sent to your Gmail with message details
4. Auto-reply sent to user thanking them
5. Success message displayed to user

## 🔒 Security Notes

- ✅ Gmail password stored in environment variables (never in code)
- ✅ Using Gmail App Passwords (more secure than account password)
- ✅ CSRF protection enabled
- ✅ DEBUG = False in production

## 🐛 Troubleshooting

### Email not sending?
1. Check terminal for error messages
2. Verify Gmail App Password is correct
3. Check if 2-Step Verification is enabled
4. Look in Gmail spam folder

### 500 Server Error?
1. Check environment variables are set
2. Run migrations: `python manage.py migrate`
3. Check Django logs in terminal

## 📞 Support

For issues, check:
- Django documentation: https://docs.djangoproject.com/
- Gmail App Passwords: https://support.google.com/accounts/answer/185833

## 📄 License

This project is open source and available for personal use.

---

Made with ❤️ by Sai Sanket
