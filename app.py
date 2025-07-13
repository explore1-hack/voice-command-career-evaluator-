import streamlit as st
from voice_input import listen_to_user
from voice_output import speak
from llm_response import get_llm_response
from memory import (
    add_answer,
    get_answers,
    reset_memory,
    add_question,
    get_question_list,
    clear_questions,
)

st.set_page_config(page_title="Career Guider AI", layout="centered")

st.title("🎯 Career Guider AI")
st.markdown("Let AI guide your career based on your personality, interests, and strengths.")

# Start session state
if "current_question" not in st.session_state:
    st.session_state.current_question = None
    st.session_state.q_count = 0
    st.session_state.total_questions = 15
    reset_memory()
    clear_questions()

# Ask first question if not started
if st.session_state.q_count == 0 and st.session_state.current_question is None:
    prompt = """You are an experienced career guide and counselor for students of all ages. 
Ask me 15 questions to evaluate my personality, interests, and skills to find a profession I'm most suited for. 
Ask questions one at a time. Start with the first question only."""
    first_q = get_llm_response(prompt)
    st.session_state.current_question = first_q
    add_question(first_q)

# Display current question
st.markdown(f"**Q{st.session_state.q_count + 1}:** {st.session_state.current_question}")
user_answer = st.text_input("Your Answer:", key=st.session_state.q_count)

if st.button("Submit Answer"):
    if user_answer.strip() == "":
        st.warning("Please enter an answer before continuing.")
    else:
        add_answer(st.session_state.current_question, user_answer)
        st.session_state.q_count += 1

        if st.session_state.q_count < st.session_state.total_questions:
            # Ask next question
            prompt = f"You are continuing a career evaluation. Ask question {st.session_state.q_count + 1} out of 15 based on prior responses. Only give the question."
            next_q = get_llm_response(prompt)
            st.session_state.current_question = next_q
            add_question(next_q)
            st.rerun()
        else:
            # Evaluate answers
            all_qa = get_answers()
            eval_prompt = "You are a career counselor. Based on these 15 questions and answers, suggest the most suitable career path:\n\n"
            for item in all_qa:
                eval_prompt += f"Q: {item['question']}\nA: {item['answer']}\n"

            eval_prompt += "\nNow analyze them and suggest:\n1. The best career match\n2. Why it suits the user\n3. 5 key strengths based on the answers\n"

            result = get_llm_response(eval_prompt)

            st.success("✅ Career Evaluation Complete!")
            st.markdown("### 🧠 AI Recommendation:")
            st.markdown(result)
            reset_memory()
            clear_questions()

if st.button("🎙️ Use Voice"):
    command = listen_to_user()

    if "start" in command:
        speak("Starting your career discovery quiz.")
        st.session_state.quiz_started = True
        st.rerun()

    elif "submit" in command:
        speak("Submitting your answers.")
        st.session_state.quiz_finished = True
        st.rerun()

    elif st.session_state.get("quiz_started") and not st.session_state.get("quiz_finished"):
        st.session_state.answers.append(command)
        speak(f"Got it. Answer recorded: {command}")
        st.rerun()
