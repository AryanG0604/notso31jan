import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Internship Assessment 💌",
    page_icon="💖",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #fff1f5, #ffe4ec);
}

.card {
    background: white;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0px 15px 40px rgba(255, 105, 180, 0.15);
    margin-top: 30px;
}

.title {
    text-align: center;
    font-size: 36px;
    font-weight: 700;
    color: #ff4b7d;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #555;
    margin-bottom: 10px;
}

.footer {
    text-align: center;
    font-size: 14px;
    color: #999;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- QUESTIONS (MCQ) ----------------
questions = [
    {
        "question": "Our fav song?",
        "options": [
            "Iris",
            "Dekha hi nahi",
            "Be my baby",
            "Agar Tum saath ho"
        ],
        "answer": "Dekha hi nahi"
    },
    {
        "question": "What would we like to do when we'll meet again?",
        "options": [
            "Just stay home and cuddle endlessly.",
            "Cook food for each other",
            "Go to a club, dressed hot, get drunk and dance our hearts out",
            "All of the above"
        ],
        "answer": "All of the above"
    },
    {
        "question": "The actual date you became my valentine?",
        "options": [
            "Mai tera",
            "Tera mai",
            "13.05.2025",
            "04.02.2026"
        ],
        "answer": "13.05.2025"
    }
]

# ---------------- SESSION STATE ----------------
if "q_index" not in st.session_state:
    st.session_state.q_index = 0

if "completed" not in st.session_state:
    st.session_state.completed = False

# ---------------- HEADER ----------------
st.markdown('<div class="title">Internship Assessment Portal</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Designed for one exceptional candidate 💖</div>', unsafe_allow_html=True)

# ---------------- PROGRESS ----------------
progress = st.session_state.q_index / (len(questions))
st.progress(progress)

# ---------------- QUESTION CARD ----------------
if st.session_state.q_index < len(questions):
    q = questions[st.session_state.q_index]

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(f"### Question {st.session_state.q_index + 1}")
    st.write(q["question"])

    choice = st.radio(
        "Choose the best answer:",
        q["options"],
        key=f"q_{st.session_state.q_index}"
    )

    if st.button("Submit ✨"):
        if choice == q["answer"]:
            st.success("Perfect ✨ Let’s move ahead…")
            st.session_state.q_index += 1
            st.rerun()
        else:
            st.warning("Almost there. Trust your heart and try again 💭")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- FINAL QUESTION ----------------
elif not st.session_state.completed:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Final Assessment 💘")
    st.write("After everything you’ve seen, answered, and felt…")
    st.markdown("## Will you be my Valentine KINSHIIII? 💖")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes 💕"):
            st.session_state.completed = True
            st.rerun()
    with col2:
        if st.button("Absolutely Yes 💖"):
            st.session_state.completed = True
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- SUCCESS SCREEN ----------------
else:
    st.balloons()
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.success("🎉 Hehe babes! You are officially My Valentine 💞(Doesn't matter Jan or Feb or any other 10 months in this calendar you are my forever valentine and you'll always be).")
    st.write("Welcome aboard. This role comes with unlimited hugs, kisses and stolen smiles")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="footer">Made with ❤️ by someone who really loves you and your forever.</div>', unsafe_allow_html=True)
