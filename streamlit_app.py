import streamlit as st

# 페이지 설정 - 모바일 최적화
st.set_page_config(
    page_title="AI 로봇을 이겨라",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 모바일 최적화 CSS 스타일
st.markdown("""
<style>
    /* 전체 텍스트 크기 및 여백 조정 */
    body {
        font-size: 18px;
        line-height: 1.8;
    }
    
    /* 메인 컨텐츠 영역 */
    .stMarkdown {
        font-size: 18px;
    }
    
    /* 제목 크기 조정 */
    h1 {
        font-size: 32px;
        margin-bottom: 20px;
    }
    
    h2 {
        font-size: 24px;
        margin-bottom: 16px;
    }
    
    h3 {
        font-size: 20px;
        margin-bottom: 12px;
    }
    
    /* 일반 텍스트 */
    p {
        font-size: 18px;
        margin-bottom: 15px;
        line-height: 1.8;
    }
    
    /* 입력 필드 크기 */
    input {
        font-size: 18px !important;
    }
    
    /* 버튼 크기 */
    button {
        font-size: 16px;
        padding: 12px;
    }
    
    /* 탭 간격 조정 */
    .stTabs {
        margin-bottom: 20px;
    }
    
    /* 섹션 간 여백 */
    .section {
        margin-bottom: 25px;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# 1. 상단 타이틀
# ============================================================
st.markdown("<h1 style='text-align: center;'>🤖 AI 로봇을 이겨라!</h1>", unsafe_allow_html=True)
st.markdown("<hr style='margin: 20px 0;'>", unsafe_allow_html=True)

# ============================================================
# 2. 상단 안내 영역
# ============================================================
st.markdown("<h3>📝 안내 사항</h3>", unsafe_allow_html=True)
st.markdown("""
#### 🎯 챌린지 설명
스마트폰 키보드의 **음성 인식(마이크) 기능**을 이용해 AI 로봇과 대결해 보세요!

#### 📱 준비하기 가이드
아래 도전 과제의 **입력 칸을 터치**한 후, 자판에 나타나는 **마이크 아이콘**을 눌러 말할 준비를 하세요!
""")

st.markdown("<hr style='margin: 25px 0;'>", unsafe_allow_html=True)

# ============================================================
# 3. 도전 과제 (탭 구성)
# ============================================================
st.markdown("<h2>🎮 도전 과제</h2>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["도전 1️⃣", "도전 2️⃣", "도전 3️⃣"])

# ============================================================
# 도전 1 탭
# ============================================================
with tab1:
    st.markdown("<h3>도전 1️⃣</h3>", unsafe_allow_html=True)
    
    # 1단계: 문장 듣기
    st.markdown("### 🎧 1단계: 잘 들으세요")
    st.markdown("아래 오디오를 재생하여 문장을 들으세요.")
    
    # 오디오 파일 경로 (필요시 수정해주세요)
    audio_file_1 = "Audio1.wav"  # 실제 파일 경로로 변경: "path/to/your/audio1.mp3"
    try:
        st.audio(audio_file_1)
    except:
        st.warning("⚠️ 오디오 파일을 찾을 수 없습니다. 파일 경로를 확인해주세요.")
    
    st.markdown("<div style='margin: 20px 0;'></div>", unsafe_allow_html=True)
    
    # 2단계: 내가 말하기
    st.markdown("### 🎤 2단계: 똑같이 말하세요")
    st.markdown("아래 입력 칸을 터치하고 스마트폰 자판의 마이크 버튼을 눌러 말해보세요.")
    user_input_1 = st.text_input(
        "음성 입력 1",
        placeholder="여기를 터치하고 자판의 마이크를 눌러 말하세요",
        key="challenge_1_input",
        label_visibility="collapsed"
    )
    
    st.markdown("<div style='margin: 20px 0;'></div>", unsafe_allow_html=True)
    
    # 3단계: 정답 확인하기
    st.markdown("### ✏️ 3단계: 똑같은지 확인하세요")
    with st.expander("정답 확인하기 👈 터치하세요"):
        # 정답 문장 (필요시 수정해주세요)
        answer_1 = "안녕하세요. 저는 학생입니다."  # 정답 문장 수정: "여기에 정답을 입력하세요"
        st.info(f"**정답:** {answer_1}")
        
        # 입력 결과 비교
        if user_input_1:
            st.write(f"**당신의 입력:** {user_input_1}")
            if user_input_1.strip().lower() == answer_1.strip().lower():
                st.success("✅ 완벽합니다! 정답입니다!")
            else:
                st.warning("⏰ 다시 한 번 말해보세요!")

st.markdown("<div style='margin: 30px 0;'></div>", unsafe_allow_html=True)

# ============================================================
# 도전 2 탭
# ============================================================
with tab2:
    st.markdown("<h3>도전 2️⃣</h3>", unsafe_allow_html=True)
    
    # 1단계: 문장 듣기
    st.markdown("### 🎧 1단계: 잘 들으세요")
    st.markdown("아래 오디오를 재생하여 문장을 들으세요.")
    
    # 오디오 파일 경로 (필요시 수정해주세요)
    audio_file_2 = "오디오2.mp3"  # 실제 파일 경로로 변경: "path/to/your/audio2.mp3"
    try:
        st.audio(audio_file_2)
    except:
        st.warning("⚠️ 오디오 파일을 찾을 수 없습니다. 파일 경로를 확인해주세요.")
    
    st.markdown("<div style='margin: 20px 0;'></div>", unsafe_allow_html=True)
    
    # 2단계: 내가 말하기
    st.markdown("### 🎤 2단계: 똑같이 말하세요")
    st.markdown("아래 입력 칸을 터치하고 스마트폰 자판의 마이크 버튼을 눌러 말해보세요.")
    user_input_2 = st.text_input(
        "음성 입력 2",
        placeholder="여기를 터치하고 자판의 마이크를 눌러 말하세요",
        key="challenge_2_input",
        label_visibility="collapsed"
    )
    
    st.markdown("<div style='margin: 20px 0;'></div>", unsafe_allow_html=True)
    
    # 3단계: 정답 확인하기
    st.markdown("### ✏️ 3단계: 똑같은지 확인하세요")
    with st.expander("정답 확인하기 👈 터치하세요"):
        # 정답 문장 (필요시 수정해주세요)
        answer_2 = "오늘 날씨가 정말 좋네요."  # 정답 문장 수정: "여기에 정답을 입력하세요"
        st.info(f"**정답:** {answer_2}")
        
        # 입력 결과 비교
        if user_input_2:
            st.write(f"**당신의 입력:** {user_input_2}")
            if user_input_2.strip().lower() == answer_2.strip().lower():
                st.success("✅ 완벽합니다! 정답입니다!")
            else:
                st.warning("⏰ 다시 한 번 말해보세요!")

st.markdown("<div style='margin: 30px 0;'></div>", unsafe_allow_html=True)

# ============================================================
# 도전 3 탭
# ============================================================
with tab3:
    st.markdown("<h3>도전 3️⃣</h3>", unsafe_allow_html=True)
    
    # 1단계: 문장 듣기
    st.markdown("### 🎧 1단계: 잘 들으세요")
    st.markdown("아래 오디오를 재생하여 문장을 들으세요.")
    
    # 오디오 파일 경로 (필요시 수정해주세요)
    audio_file_3 = "오디오3.mp3"  # 실제 파일 경로로 변경: "path/to/your/audio3.mp3"
    try:
        st.audio(audio_file_3)
    except:
        st.warning("⚠️ 오디오 파일을 찾을 수 없습니다. 파일 경로를 확인해주세요.")
    
    st.markdown("<div style='margin: 20px 0;'></div>", unsafe_allow_html=True)
    
    # 2단계: 내가 말하기
    st.markdown("### 🎤 2단계: 똑같이 말하세요")
    st.markdown("아래 입력 칸을 터치하고 스마트폰 자판의 마이크 버튼을 눌러 말해보세요.")
    user_input_3 = st.text_input(
        "음성 입력 3",
        placeholder="여기를 터치하고 자판의 마이크를 눌러 말하세요",
        key="challenge_3_input",
        label_visibility="collapsed"
    )
    
    st.markdown("<div style='margin: 20px 0;'></div>", unsafe_allow_html=True)
    
    # 3단계: 정답 확인하기
    st.markdown("### ✏️ 3단계: 똑같은지 확인하세요")
    with st.expander("정답 확인하기 👈 터치하세요"):
        # 정답 문장 (필요시 수정해주세요)
        answer_3 = "한국어는 배우기 쉬워요."  # 정답 문장 수정: "여기에 정답을 입력하세요"
        st.info(f"**정답:** {answer_3}")
        
        # 입력 결과 비교
        if user_input_3:
            st.write(f"**당신의 입력:** {user_input_3}")
            if user_input_3.strip().lower() == answer_3.strip().lower():
                st.success("✅ 완벽합니다! 정답입니다!")
            else:
                st.warning("⏰ 다시 한 번 말해보세요!")

st.markdown("<hr style='margin: 30px 0;'>", unsafe_allow_html=True)

# ============================================================
# 하단 축하 메시지
# ============================================================
st.markdown("""
<div style='text-align: center; padding: 20px; background-color: #f0f0f0; border-radius: 10px;'>
    <h2>🎉 모든 도전을 완료했나요?</h2>
    <p style='font-size: 16px;'>열심히 연습해주셔서 감사합니다!</p>
</div>
""", unsafe_allow_html=True)
