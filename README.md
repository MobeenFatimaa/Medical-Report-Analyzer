# AI Medical Report Analyzer

An intelligent web application built with **Flask** and **Google Gemini AI** that transforms complex medical reports into structured, easy-to-understand, and actionable health insights. The application extracts text from uploaded medical reports, analyzes the content using AI, identifies abnormal findings, calculates an overall health score, and generates personalized recommendations through a modern interactive dashboard.

---

## Features

- Upload and analyze medical reports in PDF format
- Automatic text extraction using OCR and PDF parsing
- AI-powered medical report interpretation using Google Gemini
- Interactive health dashboard with animated health score
- Automatic health risk assessment (Low, Moderate, High)
- AI-generated summary of the uploaded report
- Detection and explanation of abnormal findings
- Personalized health recommendations
- Interactive charts and medical statistics
- Download analyzed report as a PDF
- Contact form with Flask-Mail integration
- Modern Glassmorphism UI with responsive design

---

# Tech Stack

### Backend
- Python
- Flask
- Flask-Mail

### Artificial Intelligence
- Google Gemini API
- google-generativeai

### Frontend
- HTML5
- CSS3
- JavaScript
- Chart.js

### PDF Processing
- PyMuPDF (fitz)
- Tesseract OCR
- html2pdf.js
- html2canvas

### Utilities
- python-dotenv

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/MobeenFatimaa/Medical-Report-Analyzer.git

cd Medical-Report-Analyzer
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a file named **.env** in the project root.

```env
# ==========================
# Google Gemini
# ==========================

GEMINI_API_KEY=your_gemini_api_key_here

# ==========================
# Flask
# ==========================

SECRET_KEY=your_secret_key

# ==========================
# Flask Mail
# ==========================

MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True

MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_google_app_password
```

---

## 5. Run the Application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

# Project Structure

```text
Medical-Report-Analyzer/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── uploads/
│   └── .gitkeep
│
├── ai_analyzer.py
├── analyzer.py
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
└── LICENSE
```

---

# Workflow

1. Upload a medical report
2. Extract report text
3. Send extracted text to Google Gemini
4. AI analyzes the report
5. Generate health score
6. Detect abnormal findings
7. Create medical summary
8. Generate recommendations
9. Display results in an interactive dashboard
10. Download the analyzed report as PDF

---

# Security

- API keys are stored using **.env**
- Sensitive credentials are excluded using **.gitignore**
- Temporary uploaded files are stored locally
- No API credentials are exposed in the source code

---

# License

This project is licensed under the **Apache License 2.0**.

See the **LICENSE** file for more information.

---

# Author

**Mobeen Fatima**

GitHub:
https://github.com/MobeenFatimaa

---

## Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub.

It helps support the project and encourages future development.
