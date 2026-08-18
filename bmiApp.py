 import streamlit as st


st.markdown("# :red[🩺 คำนวณค่าดัชนีมวลกาย BMI]")
st.write("กรอกข้อมูลน้ำหนักส่วนสูงของคุณ เพื่อเช็คสุขภาพเบื้องต้น")


weight = st.number_input("กรอกน้ำหนักของคุณ (กิโลกรัม):", min_value=1.0, value=1.0)
height_cm = st.number_input("กรอกส่วนสู.ของคุณ (เซนติเมตร):, min_value=1.0, value=1.0)



if st.button("คำนวณค่า BMI                            
