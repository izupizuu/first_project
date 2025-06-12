import streamlit as st
import random

st.set_page_config(
    page_title="가위✌️바위✊보🖐️ 배틀!",
    page_icon="🕹️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 🔥 타이틀
st.markdown("<h1 style='text-align: center; color: hotpink;'>🎮 가위 ✌️ 바위 ✊ 보 🖐️ 배틀!</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: gold;'>🤖 컴퓨터를 이겨보세요! 🎯</h3>", unsafe_allow_html=True)
st.markdown("---")

# 🎲 선택지
choices = {
    "가위 ✌️": "✌️",
    "바위 ✊": "✊",
    "보 🖐️": "🖐️"
}

# 🧑 사용자 입력
st.markdown("## 🧍 당신의 선택은?")
user_choice = st.columns(3)
user_selection = None

with user_choice[0]:
    if st.button("✌️ 가위"):
        user_selection = "✌️"
with user_choice[1]:
    if st.button("✊ 바위"):
        user_selection = "✊"
with user_choice[2]:
    if st.button("🖐️ 보"):
        user_selection = "🖐️"

# 🖥️ 컴퓨터 선택
if user_selection:
    computer_selection = random.choice(["✌️", "✊", "🖐️"])
    
    st.markdown("---")
    st.markdown("### ⚔️ 결과")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 🧍 당신")
        st.markdown(f"<div style='font-size:60px; text-align:center'>{user_selection}</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("#### 🤖 컴퓨터")
        st.markdown(f"<div style='font-size:60px; text-align:center'>{computer_selection}</div>", unsafe_allow_html=True)

    # 🏆 결과 판단
    def get_winner(user, comp):
        if user == comp:
            return "🤝 비겼습니다!"
        elif (user == "✌️" and comp == "🖐️") or (user == "✊" and comp == "✌️") or (user == "🖐️" and comp == "✊"):
            return "🎉 당신이 이겼어요!"
        else:
            return "😢 컴퓨터가 이겼습니다..."

    result = get_winner(user_selection, computer_selection)
    st.markdown(f"<h2 style='text-align: center; color: deepskyblue'>{result}</h2>", unsafe_allow_html=True)
    st.balloons()

st.markdown("---")
st.markdown("<p style='text-align: center;'>💡 새로고침하거나 다른 버튼을 눌러 다시 시도하세요!</p>", unsafe_allow_html=True)
