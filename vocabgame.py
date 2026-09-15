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
        st.error("💀 you lose")

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
    "ข้อ 2: `b _ _ e` is a piece of skeleton.",
    value=st.session_state.ans2_val,
    key="input2"
)
ans3 = st.text_input(
    "ข้อ 3: The `d _ c _ _ r` is a job to cure patient.",
    value=st.session_state.ans3_val,
    key="input3"
)
ans4 = st.text_input(
    "ข้อ 4: Be quiet, the `st _ d _ nt` is learning.",
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
st.write("นายกฤตภาส สายทอง ม.4/12 เลขที่ 36")        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

    # ตรวจข้อ 2
    if u_ans2 == "fish":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

    # ✏️ [พื้นที่สำหรับนักเรียน]: เพิ่มตรวจข้อ 3, 4 ตรงนี้

    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")

    if score == 2:
        st.success("🎉 You win!")
    else:
        st.error("💀 You lose!")


# ----------------------------------------------------
# 1. ปุ่มเริ่มเล่นเกม
# ----------------------------------------------------
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

# 2. แถบแสดงเวลานับถอยหลัง
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(30 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# 3. ช่องรับคำตอบ (ใช้ value ผูกกับตัวแปรตรงๆ เพื่อสั่งเคลียร์ได้)
ans1 = st.text_input(
    "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎",
    value=st.session_state.ans1_val,
)
ans2 = st.text_input(
    "ข้อ 2: Cats love to eat `f _ s h`. 🐟",
    value=st.session_state.ans2_val,
)

# อัปเดตค่าล่าสุดเข้าตัวแปร
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2

# ✏️ [พื้นที่สำหรับนักเรียน]: เพิ่มข้อ 3, 4 ตรงนี้


# 4. ปุ่มส่งคำตอบ
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
