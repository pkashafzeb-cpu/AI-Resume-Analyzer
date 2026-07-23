import os
from google import genai
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Check if API key exists
if not API_KEY:
    print("❌ Error: GEMINI_API_KEY not found in .env file!")
    print("Please add your Gemini API key to the .env file.")
    exit()

# Create Gemini client with the new SDK
client = genai.Client(api_key=API_KEY)


def analyze_resume(resume_text):
    """
    Send resume text to Gemini AI and get professional feedback.
    """
    prompt = f"""
    You are an expert resume reviewer and career coach with 10+ years of experience.
    
    Analyze the following resume and provide detailed, actionable feedback.

    Resume Text:
    ---
    {resume_text}
    ---

    Please provide feedback in this exact structure:

    1. OVERALL IMPRESSION (2-3 lines)
    
    2. KEY STRENGTHS (bullet points)
    
    3. WEAKNESSES / GAPS (bullet points)
    
    4. SPECIFIC IMPROVEMENTS (numbered list with clear actions)
    
    5. ATS COMPATIBILITY SCORE (out of 100 with reasoning)
    
    Be honest, professional, and specific.
    """

    try:
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt,
            config={
                "temperature": 0.7,
                "max_output_tokens": 1500
            }
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"


# ===================== TESTING =====================
if __name__ == "__main__":
    print("🤖 AI Resume Analyzer - Day 2 Test\n")
    print("=" * 60)

    # Sample resume for testing
    sample_resume = """
    John Doe
    Email: john.doe@email.com | Phone: +1-234-567-8900
    LinkedIn: linkedin.com/in/johndoe

    EDUCATION:
    Bachelor of Technology in Data Science
    XYZ University (2019-2023) | GPA: 3.7/4.0

    EXPERIENCE:
    Data Analyst | ABC Corp (June 2023 - Present)
    - Analyzed customer data using SQL and Python
    - Built dashboards in Power BI
    - Presented insights to stakeholders

    Data Science Intern | XYZ Ltd (May 2022 - August 2022)
    - Worked on machine learning models
    - Cleaned and processed datasets

    SKILLS:
    Python, SQL, Excel, Power BI, Machine Learning, Pandas, NumPy

    PROJECTS:
    - Customer Churn Prediction Model
    - Sales Forecasting Dashboard
    """

    print("Analyzing sample resume with Gemini AI...\n")
    print("=" * 60)
    
    feedback = analyze_resume(sample_resume)
    
    print(feedback)
    print("\n" + "=" * 60)
    print("✅ Analysis complete!")