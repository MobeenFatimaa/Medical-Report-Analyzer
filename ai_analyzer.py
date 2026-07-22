
import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure Gemini with environment variable
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")


def analyze_report(report_text):
    prompt = f"""
You are an expert medical AI assistant.

Analyze the following medical report.

Return ONLY valid JSON.

Use this exact structure:

{{
  "health_score": 92,
  "summary": "",
  "abnormal_values": [
    {{
      "name": "",
      "status": "",
      "reason": ""
    }}
  ],
  "recommendations": [
    "",
    "",
    ""
  ]
}}

Medical Report:

{report_text}
"""

    response = model.generate_content(prompt)

    clean_text = response.text.strip()

    # Remove Markdown code fences if Gemini returns them
    if clean_text.startswith("```json"):
        clean_text = clean_text.replace("```json", "", 1)

    if clean_text.startswith("```"):
        clean_text = clean_text.replace("```", "", 1)

    if clean_text.endswith("```"):
        clean_text = clean_text[:-3]

    clean_text = clean_text.strip()

    print("========== CLEAN JSON ==========")
    print(clean_text)
    print("================================")

    return json.loads(clean_text)
