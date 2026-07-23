# 🤖 AI Resume Analyzer

An AI-powered resume analysis tool designed to provide professional feedback, identify resume weaknesses, and suggest actionable improvements using the Google Gemini API.

---

## 📌 Project Overview

The **AI Resume Analyzer** uses a Large Language Model (LLM) to evaluate resume content and provide feedback such as:

- Overall resume impression
- Key candidate strengths
- Weak or missing information
- Skills identified in the resume
- Specific and actionable improvements
- ATS-friendly recommendations

This project is part of my AI learning journey and demonstrates practical experience with:

- LLM API integration
- Prompt engineering
- Secure API-key management
- Python application development
- Git and GitHub
- AI application deployment

---

## 🛠️ Technology Stack

| Category | Technology |
|---|---|
| Programming language | Python 3.12 |
| AI model | Google Gemini |
| SDK | `google-genai` |
| Environment variables | `python-dotenv` |
| PDF processing | `pdfplumber` — planned |
| Web interface | Streamlit — planned |
| Version control | Git and GitHub |

---

## ✨ Current Features

- [x] Gemini API integration
- [x] Command-line resume analysis
- [x] Structured resume feedback
- [x] Identification of strengths and weaknesses
- [x] ATS-friendly recommendations
- [x] Secure API-key management using `.env`
- [x] Fictional sample resume for safe testing
- [ ] PDF resume upload
- [ ] PDF text extraction
- [ ] Structured JSON response
- [ ] ATS compatibility scoring
- [ ] Skills-gap analysis
- [ ] Resume and job-description comparison
- [ ] Streamlit web application
- [ ] Downloadable PDF analysis report
- [ ] Cloud deployment

---

## 📅 Development Progress

### ✅ Day 1 — Project Setup

- Created the initial project structure
- Created a Python virtual environment
- Initialized the Git repository
- Configured `.gitignore`
- Added secure environment-variable management
- Created the initial project documentation
- Pushed the first commit to GitHub

### ✅ Day 2 — Gemini API Integration

- Migrated to the current `google-genai` SDK
- Connected the application to the Gemini API
- Created a working command-line resume analyzer
- Added a fictional sample resume for testing
- Learned how LLM API requests and responses work
- Learned about tokens, context windows, and output-token limits
- Experimented with temperature and output length
- Protected the Gemini API key using `.env`
- Added API error handling

### 🔜 Day 3 — Prompt Engineering and Streamlit

### ✅ Day 3 — Prompt Engineering Experiments

**Achievements:**
- Built an interactive **Streamlit Prompt Playground**
- Implemented **three prompt-engineering techniques**:
  - Zero-shot prompting
  - Role + Structured prompting
  - Few-shot prompting
- Added editable prompt area for custom experimentation
- Added token usage tracking
- Ran controlled experiments comparing all three techniques
- Documented findings in `prompt_experiments.md`
- Selected **Role + Structured Prompting** as the winning technique

**Experiment Results:**

| Technique | Format Quality | Content Quality | Tokens Used | Verdict |
|---|---|---|---|---|
| Zero-shot | Moderate | Inconsistent | 993 | Fast but unreliable |
| Role + Structured | Excellent | Excellent | 1,205 | ⭐ **Winner** |
| Few-shot | Perfect | Less detailed | 812 | Consistent but shallow |

**Key Finding:** Adding a professional role ("You are an expert recruiter...") combined with structured output requirements produced the most detailed, honest, and actionable feedback. Structure alone (Few-shot) was not enough — content quality matters more.

### 🔜 Day 4 — PDF Upload and Real Resume Analysis (Coming Next)

Planned tasks:

- Add PDF file upload support
- Integrate `pdfplumber` for text extraction
- Handle scanned and non-standard PDFs
- Build a production-ready analyzer UI
- Apply Role + Structured prompting (winning technique)

---

## 🧠 How the Current Version Works

```text
Fictional or anonymized resume text
                  ↓
        Resume-analysis prompt
                  ↓
            Gemini API
                  ↓
     AI-generated resume feedback
                  ↓
        Displayed in the terminal
```

The current application sends resume text to Gemini and requests feedback using clearly defined sections.

---

## 📋 Current Analysis Sections

The command-line application currently generates:

1. **Overall Impression**
2. **Key Strengths**
3. **Weak or Missing Information**
4. **Skills Identified**
5. **Recommended Improvements**
6. **ATS-Friendly Suggestions**

---

## 📁 Project Structure

```text
AI-Resume-Analyzer/
│
├── .venv/                  # Local virtual environment
├── .env                    # Private Gemini API key
├── .env.example            # Safe environment-variable template
├── .gitignore              # Files excluded from Git
├── day2_llm_test.py        # Current resume-analysis script
├── gemini_test.py          # Gemini API connection test
├── day1_notes.md           # Day 1 learning notes
├── day2_notes.md           # Day 2 learning notes
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

> `.venv/` and `.env` are stored locally and are not uploaded to GitHub.

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/pkashafzeb-cpu/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

### 2. Create a virtual environment

```bash
py -m venv .venv
```

### 3. Activate the environment

#### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

#### Windows Command Prompt

```cmd
.venv\Scripts\activate.bat
```

### 4. Install the dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Configure the Gemini API key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

You can copy the included example file:

```bash
copy .env.example .env
```

Then replace the placeholder with your actual Gemini API key.

### 6. Run the Gemini connection test

```bash
python gemini_test.py
```

### 7. Run the Resume Analyzer

```bash
python day2_llm_test.py
```

---

## ⚙️ Generation Parameters

The application experiments with two important LLM parameters.

### Temperature

Temperature controls how varied or predictable the generated response is.

| Temperature | Typical behavior |
|---:|---|
| `0.2` | More focused and consistent |
| `0.7` | Balanced variation |
| `1.0` | More varied output |

Resume analysis generally benefits from focused and consistent output. However, the final setting should be selected through testing.

### Maximum Output Tokens

The maximum output-token setting limits how long the generated response can be.

| Token limit | Typical result |
|---:|---|
| `300` | Short response; sections may be incomplete |
| `700` | Moderate amount of feedback |
| `1000` | Detailed resume analysis |
| `1200+` | Longer response, possibly repetitive |

---

## 🔬 Parameter Experiments

| Temperature | Maximum output tokens | Observation |
|---:|---:|---|
| `0.2` | `800` | Add your observation |
| `0.7` | `800` | Add your observation |
| `1.0` | `800` | Add your observation |
| `0.3` | `300` | Add your observation |
| `0.3` | `1200` | Add your observation |

These experiments help determine which configuration produces the most useful, accurate, and consistent resume feedback.

---

## 🔐 Privacy and Security

This project follows the following security practices:

- The Gemini API key is stored inside `.env`
- `.env` is excluded from Git using `.gitignore`
- The API key is never written directly into the Python code
- Only fictional or anonymized resumes are used during development
- Private resumes are not stored in the repository
- The virtual environment is not uploaded to GitHub

> Never upload your `.env` file, API key, or private resume data to GitHub.

---

## 🗺️ Project Roadmap

### Phase 1 — Foundation

- [x] Set up the Python project
- [x] Configure Git and GitHub
- [x] Integrate the Gemini API
- [x] Build a command-line prototype

### Phase 2 — Prompt Engineering

- [ ] Compare zero-shot and few-shot prompts
- [ ] Improve system instructions
- [ ] Add prompt constraints
- [ ] Add structured JSON output
- [ ] Validate the generated response

### Phase 3 — Resume Processing

- [ ] Add PDF upload
- [ ] Extract text using `pdfplumber`
- [ ] Clean extracted resume text
- [ ] Handle invalid or scanned PDF files

### Phase 4 — Advanced Analysis

- [ ] Calculate ATS compatibility
- [ ] Detect missing resume sections
- [ ] Compare a resume with a job description
- [ ] Identify skills gaps
- [ ] Generate role-specific recommendations

### Phase 5 — Product and Deployment

- [ ] Build a Streamlit interface
- [ ] Add a downloadable report
- [ ] Improve error handling
- [ ] Add screenshots and an architecture diagram
- [ ] Deploy the application

---

## ⚠️ Current Limitations

- The current version accepts text rather than uploaded PDF files
- ATS scoring has not yet been implemented
- The analysis depends on the quality of the supplied resume text
- LLM feedback should be treated as guidance, not a hiring decision
- The application is currently a learning prototype

---

## 🎯 Learning Outcomes

Through this project, I am learning how to:

- Build applications powered by LLM APIs
- Design and evaluate prompts
- Protect API keys and sensitive information
- Handle temporary API errors
- Organize a professional Python repository
- Document project progress
- Convert an AI prototype into a deployable application

---

## 👩‍💻 Author

**Parkha Kashaf Zeb**

Data Science student focused on building practical applications using:

- Python
- Machine Learning
- Data Analytics
- Large Language Models
- Retrieval-Augmented Generation
- AI Agents

---

## 📄 Disclaimer

This application is an educational project. Its feedback should be reviewed by the user and should not replace professional career advice or human resume evaluation.