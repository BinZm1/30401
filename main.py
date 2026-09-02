import random
import streamlit as st

# 역할군별 캐릭터 목록 정의
heroes = {
    "탱커": [
        "디몬", "디바", "도미나", "둠피스트", "라마트라", "라인하르트", 
        "레킹볼", "로드호그", "마우가", "시그마", "오리사", "윈스턴", 
        "자리야", "정커퀸", "해저드"
    ],
    "딜러": [
        "겐지", "리퍼", "메이", "바스티온", "벤데타", "벤처", "소전", 
        "솔저: 76", "솜브라", "시메트라", "시에라", "시온", "안란", "애쉬", 
        "에코", "엠레", "위도우메이커", "정크랫", "캐서디", "토르비욘", 
        "트레이서", "파라", "프레야", "한조"
    ],
    "힐러": [
        "라이프위버", "루시우", "메르시", "모이라", "미즈키", "바티스트", 
        "브리기테", "아나", "우양", "일리아리", "제트팩 캣", "젠야타", 
        "주노", "키리코"
    ]
}

# 페이지 기본 설정
st.set_page_config(page_title="오버워치 영웅 뽑기", page_icon="🎮", layout="centered")

# 오버워치 다크 스타일 커스텀 CSS (배경 및 스타일 디자인)
st.markdown("""
    <style>
    /* 전체 배경 설정 (다크 사선 패턴) */
    .stApp {
        background-color: #1A1C23;
        background-image: repeating-linear-gradient(
            45deg,
            #1A1C23,
            #1A1C23 15px,
            #21242D 15px,
            #21242D 30px
        );
    }
    
    /* 타이틀 스타일 */
    .main-title {
        text-align: center;
        font-family: 'Impact', sans-serif;
        font-size: 2.8rem;
        color: #F57C00;
        margin-bottom: 5px;
        text-shadow: 2px 2px 4px #000000;
    }
    
    .sub-title {
        text-align: center;
        color: #A0A5B5;
        margin-bottom: 30px;
    }
    
    /* 결과 카드 박스 */
    .result-card {
        background-color: #0F1015;
        border: 2px solid #F57C00;
        border-radius: 12px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 0 15px rgba(245, 124, 0, 0.4);
        margin-bottom: 30px;
    }
    
    .role-badge {
        font-size: 1.2rem;
        font-weight: bold;
        margin-bottom: 10px;
    }
    
    .hero-name {
        font-size: 2.5rem;
        font-weight: bold;
        color: #FFFFFF;
    }
    </style>
""", unsafe_allow_html=True)

# 헤더 표시
st.markdown('<div class="main-title">OVERWATCH HERO PICKER</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">원하는 역할군을 선택하여 영웅을 뽑아보세요!</div>', unsafe_allow_html=True)

# 상태 저장 (뽑힌 캐릭터 기억)
if "selected_role" not in st.session_state:
    st.session_state.selected_role = "READY"
    st.session_state.selected_hero = "?"
    st.session_state.badge_color = "#F57C00"

# 결과 카드 표시
st.markdown(f"""
    <div class="result-card">
        <div class="role-badge" style="color: {st.session_state.badge_color};">[ {st.session_state.selected_role} ]</div>
        <div class="hero-name">{st.session_state.selected_hero}</div>
    </div>
""", unsafe_allow_html=True)

# 역할군 선택 버튼 그리드
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🛡️ 탱커", use_container_width=True):
        st.session_state.selected_role = "탱커"
        st.session_state.selected_hero = random.choice(heroes["탱커"])
        st.session_state.badge_color = "#2B8CBE"
        st.rerun()

with col2:
    if st.button("⚔️ 딜러", use_container_width=True):
        st.session_state.selected_role = "딜러"
        st.session_state.selected_hero = random.choice(heroes["딜러"])
        st.session_state.badge_color = "#E65100"
        st.rerun()

with col3:
    if st.button("💉 힐러", use_container_width=True):
        st.session_state.selected_role = "힐러"
        st.session_state.selected_hero = random.choice(heroes["힐러"])
        st.session_state.badge_color = "#2E7D32"
        st.rerun()

with col4:
    if st.button("🎲 전체", use_container_width=True):
        all_heroes = heroes["탱커"] + heroes["딜러"] + heroes["힐러"]
        picked = random.choice(all_heroes)
        # 역할군 찾기
        for role, h_list in heroes.items():
            if picked in h_list:
                actual_role = role
                break
        
        colors = {"탱커": "#2B8CBE", "딜러": "#E65100", "힐러": "#2E7D32"}
        st.session_state.selected_role = actual_role
        st.session_state.selected_hero = picked
        st.session_state.badge_color = colors[actual_role]
        st.rerun()
