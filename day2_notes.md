 # Day 2 Notes - LLM API Integration

Date: [Today's date]

## 🎯 What I Learned Today

### LLM Basics
- LLMs are advanced "autocomplete" systems trained on massive text data
- They predict the next word based on patterns
- Different models have different strengths and speeds

### API Integration
- Successfully integrated Google Gemini API
- Migrated from old `google-generativeai` to new `google-genai` SDK
- Learned to use `gemini-flash-latest` model

### Tokens
- 1 token ≈ 0.75 words in English
- Input tokens = my prompt + resume text
- Output tokens = AI's response
- Controlled with `max_output_tokens`

### Temperature
- Controls creativity/randomness (0.0 to 2.0)
- Low (0.0-0.3) = focused, consistent, factual
- Medium (0.5-0.7) = balanced, professional
- High (1.0+) = creative, varied, unpredictable

### Security
- API keys must be kept in `.env` files
- `.env` must be in `.gitignore`
- Never hardcode secrets in source code

## 🛠️ What I Built

- Working Python script that connects to Gemini
- Resume analyzer that provides structured feedback
- Tested different temperature and token configurations

## 🧪 Experiments I Ran

- [x] Tested temperature 0.0 vs 0.7 vs 1.2
- [x] Tested max_output_tokens 100 vs 1500
- [x] Tried analyzing my own resume
- [x] Handled API errors gracefully

## 🐛 Challenges & Solutions

**Challenge:** `google-generativeai` was deprecated  
**Solution:** Migrated to new `google-genai` package

**Challenge:** `gemini-2.5-flash` model not found  
**Solution:** Switched to `gemini-flash-latest` alias

## 📈 Next Steps (Day 3)

- Deep dive into prompt engineering techniques
- Build Streamlit UI for the analyzer
- Add PDF upload functionality
- Improve the prompt to get better structured output
