Here’s a professional and beginner-friendly README.md file tailored for your Day 14 Career Guide AI Project on GitHub:


---

# 🧠 Voice-Controlled Career Guide AI (Day 14)

Welcome to **Career Guide AI**, a voice-enabled career suggestion chatbot built with **Streamlit**, **LLMs**, and **Speech Recognition**. This app simulates a smart career counselor who asks questions, listens to your answers (voice/text), and finally suggests the best career path for you – **completely personalized**.

---

## 🎯 Project Goal

To build an **intelligent, interactive, and voice-controlled** LLM app that:
- Asks users 15 meaningful behavioral questions
- Accepts voice/text answers
- Evaluates answers with an LLM model
- Suggests a suitable career based on traits & preferences
- Gives **voice-based feedback**

---

## 🚀 Features

✅ 15 dynamic career-detecting questions  
✅ Role-based memory storage (question + user answer)  
✅ LLM-based final analysis & profession suggestion  
✅ Voice control:
- Say `"start"` to begin quiz
- Say answers instead of typing
- Say `"submit"` to finish
✅ Voice output (AI reads the career result out loud)

---

## 🛠️ Tech Stack

| Tech | Usage |
|------|-------|
| `Python` | Core logic |
| `Streamlit` | Frontend GUI |
| `Together AI` | LLM API backend |
| `speech_recognition` | Voice input |
| `pyttsx3` | Voice output (text-to-speech) |
| `.env` | API key storage |
| `json` & `txt` | Memory & logs |

---

## 📁 Folder Structure

day14/ │ ├── app.py                # Streamlit main app ├── llm_response.py       # Handles API call to Together AI ├── memory.py             # Stores Q&A session memory ├── prompt.py             # LLM prompt template ├── voice_input.py        # Speech recognition for user input ├── voice_output.py       # TTS voice for AI response ├── requirements.txt      # Required Python packages └── .env                  # API key (excluded in .gitignore)

---

## 🔐 .env Format

Create a `.env` file:

TOGETHER_API_KEY=your_api_key_here

---

## ▶️ How to Run

```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Run the Streamlit app
streamlit run app.py


---

🧪 Demo Flow

1. Click 🎙️ Use Voice or use text input


2. Say start to begin


3. Answer 15 questions using voice


4. Say submit when done


5. AI evaluates and speaks out your career




---

🤖 Sample Careers Suggested

Software Developer

Public Speaker

Designer

Psychologist

Doctor

Teacher
...and more based on your behavior



---

🧠 Inspired By

OpenAI ChatGPT Prompt Engineering

Career Counseling Techniques

Streamlit AI App Tutorials



---

🙋‍♂️ Author

Ashutosh Pandey
GitHub: @explore1-hack
LinkedIn: Ashutosh Pandey


---

📄 License

This project is open-source and available under the MIT License.

---

Would you also like a thumbnail and banner for your Day 14 GitHub repo or YouTube demo?