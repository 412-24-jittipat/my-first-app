import time
import streamlit as st

st.title("⏱️ Word Timing Game")

# Initialize Session State Variables
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""
if "is_ended" not in st.session_state:
    st.session_state.is_ended = False

# Function to reset the game state
def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.start = time.time()
    st.session_state.is_ended = False

# ----------------------------------------------------
# 📌 MessageBox Function (Dialog)
# ----------------------------------------------------
@st.dialog("📊 Game Result")
def show_result_dialog(ans1, ans2, ans3, ans4):
    st.balloons()
    score = 0
    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()

    # Question 1 Check
    if u_ans1 == "apple":
        st.success("✅ ข้อ 1: Correct")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: Wrong (you entered '{u_ans1}')")

    # Question 2 Check
    if u_ans2 == "bone":
        st.success("✅ ข้อ 2: Correct")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: Wrong (you entered '{u_ans2}')")

    # Question 3 Check
    if u_ans3 == "doctor":
        st.success("✅ ข้อ 3: Correct")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: Wrong (you entered '{u_ans3}')")

    # Question 4 Check
    if u_ans4 == "student":
        st.success("✅ ข้อ 4: Correct")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: Wrong (you entered '{u_ans4}')")

    # Final Score
    st.divider()
    st.info(f"🏆 You scored: {score} / 4 points")
    if score == 4:
        st.success("🎉 You win!")
    else:
        st.error("💀 Bruh")

# ----------------------------------------------------
# 1. Play Button
# ----------------------------------------------------
st.button("🎮 Play", on_click=reset_game)

# ----------------------------------------------------
# 2. Countdown Display
# ----------------------------------------------------
if "start" in st.session_state and not st.session_state.is_ended:
    time_left = int(30 - (time.time() - st.session_state.start))
    if time_left > 0:
        st.error(f"⏳ Time Left: {time_left} seconds")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# ----------------------------------------------------
# 3. Answer Inputs
# ----------------------------------------------------
ans1 = st.text_input(
    "ข้อ 1: An `a _ _ l e` fell from the tree.",
    value=st.session_state.ans1_val,
    key="input1"
)
ans2 = st.text_input(
    "ข้อ 2: Dogs love to eat `b _ _ e`.",
    value=st.session_state.ans2_val,
    key="input2"
)
ans3 = st.text_input(
    "ข้อ 3: The `d _ c _ _ r` is a job.",
    value=st.session_state.ans3_val,
    key="input3"
)
ans4 = st.text_input(
    "ข้อ 4:  the `st _ d _ nt` is in school.",
    value=st.session_state.ans4_val,
    key="input4"
)

# Sync inputs to session state
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4

# ----------------------------------------------------
# 4. Enter / Submit Button
# ----------------------------------------------------
if "start" in st.session_state and not st.session_state.is_ended:
    if st.button("📥 Enter"):
        st.session_state.is_ended = True
        st.rerun()

# ----------------------------------------------------
# 5. Show Result Dialog
# ----------------------------------------------------
if st.session_state.is_ended:
    show_result_dialog(
        st.session_state.ans1_val,
        st.session_state.ans2_val,
        st.session_state.ans3_val,
        st.session_state.ans4_val
    )

st.divider()
st.write("นายจิตติพัตน์ กาละนิโย ม.4/12 เลขที่ 24")
