import os
from flask import Flask, render_template, request, redirect, flash, url_for
from flask_mail import Mail, Message
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

from analyzer import extract_text
from ai_analyzer import analyze_report

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Secret key for secure sessions
app.secret_key = os.getenv("SECRET_KEY", "fallback-secret-key-for-dev-only")

# Configure Upload Folder
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# -----------------------------
# Flask-Mail Configuration
# -----------------------------
app.config["MAIL_SERVER"] = os.getenv("MAIL_SERVER", "smtp.gmail.com")
app.config["MAIL_PORT"] = int(os.getenv("MAIL_PORT", 587))
app.config["MAIL_USE_TLS"] = os.getenv("MAIL_USE_TLS", "True") == "True"
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")

mail = Mail(app)

# -----------------------------
# Routes
# -----------------------------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    if "report" not in request.files:
        return redirect(url_for("home"))

    file = request.files["report"]

    if file.filename == "":
        return redirect(url_for("home"))

    filename = secure_filename(file.filename)
    save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)

    # Save file locally before processing
    file.save(save_path)

    # Extract text & generate analysis
    text = extract_text(save_path)
    analysis = analyze_report(text)

    return render_template("result.html", analysis=analysis)


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    user_message = request.form.get("message")

    msg = Message(
        subject=f"New Website Inquiry from {name}",
        sender=app.config["MAIL_USERNAME"],
        recipients=[app.config["MAIL_USERNAME"]]
    )

    msg.body = f"""
New Contact Form Submission
--------------------------------
Name: {name}
Email: {email}
--------------------------------
Message:
{user_message}

--------------------------------
Sent from AI Medical Report Analyzer Website
"""
    mail.send(msg)

    return redirect(url_for("home", success="true"))


# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)