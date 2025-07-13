# import os
# from datetime import datetime

# # File paths
# ANSWER_FILE = "answers.txt"
# QUESTIONS_FILE = "questions.txt"

# # Store each answer with timestamp
# def add_answer(question, answer):
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     with open(ANSWER_FILE, "a", encoding="utf-8") as f:
#         f.write(f"[{timestamp}] Q: {question}\nA: {answer}\n\n")

# # Get all stored answers
# def get_answers():
#     if not os.path.exists(ANSWER_FILE):
#         return []
#     with open(ANSWER_FILE, "r", encoding="utf-8") as f:
#         return f.readlines()

# # Reset all saved answers
# def reset_memory():
#     if os.path.exists(ANSWER_FILE):
#         os.remove(ANSWER_FILE)
#     if os.path.exists(QUESTIONS_FILE):
#         os.remove(QUESTIONS_FILE)

# # Store all 15+ questions (only once at startup)
# def store_questions(question_list):
#     with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
#         for q in question_list:
#             f.write(q.strip() + "\n")

# # Retrieve a specific question by index
# def get_question(index):
#     if not os.path.exists(QUESTIONS_FILE):
#         return None
#     with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
#         questions = f.readlines()
#         if 0 <= index < len(questions):
#             return questions[index].strip()
#         return None
# [
#   {"question": "Do you prefer working alone or in teams?", "answer": "I love working in teams."},
#   ...
# ]
import os
import json

ANSWERS_FILE = "answers.json"
QUESTIONS_FILE = "questions.json"

# ----------------------
# Answers Functions
# ----------------------

def add_answer(question, answer):
    answers = get_answers()
    answers.append({"question": question, "answer": answer})
    with open(ANSWERS_FILE, "w") as f:
        json.dump(answers, f, indent=2)

def get_answers():
    if os.path.exists(ANSWERS_FILE):
        with open(ANSWERS_FILE, "r") as f:
            return json.load(f)
    return []

def reset_memory():
    if os.path.exists(ANSWERS_FILE):
        os.remove(ANSWERS_FILE)

# ----------------------
# Questions Functions
# ----------------------

def add_question(question):
    questions = get_question_list()
    questions.append(question)
    with open(QUESTIONS_FILE, "w") as f:
        json.dump(questions, f, indent=2)

def get_question_list():
    if os.path.exists(QUESTIONS_FILE):
        with open(QUESTIONS_FILE, "r") as f:
            return json.load(f)
    return []

def clear_questions():
    if os.path.exists(QUESTIONS_FILE):
        os.remove(QUESTIONS_FILE)
