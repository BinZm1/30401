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

# 역할군 기본 색상
ROLE_COLORS = {
    "탱커": "#2B8CBE",  # 파란색
    "딜러": "#B71C1C",  # 어두운 빨간색
    "힐러": "#4CAF50"   # 밝은 초록색
}

# 갈색 테두리 (추천 안함) 영웅 목록
BROWN_HEROES = [
    # 탱커
    "로드호그", "라인하르트", "둠피스트", "정커퀸",
    # 딜러
    "위도우메이커", "캐서디", "토르비욘",
    # 힐러
    "라이프위버", "일리아리", "모이라", "메르시",
]

# 골드색 테두리 (추천함) 영웅 목록
GOLD_HEROES = [
    # 탱커
    "디몬", "시그마", "자리야", "오리사", "마우가", "라마트라",
    # 딜러
    "소전", "파라", "프레야", "엠레", "시온", "안란", "시에라", 
    # 힐러
    "키리코", "아나", "젠야타", "우양", "바티스트",
]

BROWN_COLOR = "#8B4513"  # 갈색
GOLD_COLOR = "#FFD700"   # 골드색

def get_hero_info(role_name, hero_name):
    """
    영웅 이름을 판별하여 (표시할 역할군/상태 텍스트, 테두리 색상) 튜플을 반환합니다.
    """
    # 1. 골드 추천 영웅 체크
    if hero_name in GOLD_HEROES:
        return "⭐ 추천함", GOLD_COLOR
    
    # 2. 갈색 비추천 영웅 체크
    if hero_name in BROWN_HEROES:
        return "⚠️ 추천안함", BROWN_COLOR
    
    # 3. 일반 영웅 체크
    base_role = role_name.split()[0].replace("1.", "").replace("2.", "").replace("3.", "").strip()
    return role_name, ROLE_COLORS.get(base_role, "#F57C00")

# 페이지 기본 설정
st.set_page_config(page_title="오버워치 영웅 뽑기", page_icon="🎮", layout="centered")

# 오버워치 다크 스타일 커스텀 CSS
st.markdown("""
    <style>
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
    
    .result-card {
        background-color: #0F1015;
        border: 3px solid #F57C00;
        border-radius: 12px;
        padding: 20px 10px;
        text-align: center;
        box-shadow: 0 0 12px rgba(245, 124, 0, 0.3);
    }
    
    .role-badge {
        font-size: 1rem;
        font-weight: bold;
        margin-bottom: 8px;
    }
    
    .hero-name {
        font-size: 1.5rem;
        font-weight: bold;
        color: #FFFFFF;
        word-break: keep-all;
    }
    </style>
""", unsafe_allow_html=True)

# 헤더 표시
st.markdown('<div class="main-title">OVERWATCH HERO PICKER</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">버튼을 눌러 영웅 3명을 무작위로 뽑아보세요!</div>', unsafe_allow_html=True)

# 초기 세션 상태 설정
if "results" not in st.session_state:
    st.session_state.results = [
        {"role": "READY", "hero": "?", "color": "#F57C00"},
        {"role": "READY", "hero": "?", "color": "#F57C00"},
        {"role": "READY", "hero": "?", "color": "#F57C00"}
    ]

# 3개의 결과 카드 표시
cols = st.columns(3)
for idx, item in enumerate(st.session_state.results):
    with cols[idx]:
        st.markdown(f"""
            <div class="result-card" style="border-color: {item['color']}; box-shadow: 0 0 14px {item['color']}77;">
                <div class="role-badge" style="color: {item['color']};">[ {item['role']} ]</div>
                <div class="hero-name">{item['hero']}</div>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 버튼 영역
b_col1, b_col2, b_col3, b_col4 = st.columns(4)

with b_col1:
    if st.button("🛡️ 탱커 3명", use_container_width=True):
        picked = random.sample(heroes["탱커"], 3)
        res_list = []
        for i in range(3):
            role_text, color = get_hero_info(f"탱커 {i+1}", picked[i])
            res_list.append({"role": role_text, "hero": picked[i], "color": color})
        st.session_state.results = res_list
        st.rerun()

with b_col2:
    if st.button("⚔️ 딜러 3명", use_container_width=True):
        picked = random.sample(heroes["딜러"], 3)
        res_list = []
        for i in range(3):
            role_text, color = get_hero_info(f"딜러 {i+1}", picked[i])
            res_list.append({"role": role_text, "hero": picked[i], "color": color})
        st.session_state.results = res_list
        st.rerun()

with b_col3:
    if st.button("💉 힐러 3명", use_container_width=True):
        picked = random.sample(heroes["힐러"], 3)
        res_list = []
        for i in range(3):
            role_text, color = get_hero_info(f"힐러 {i+1}", picked[i])
            res_list.append({"role": role_text, "hero": picked[i], "color": color})
        st.session_state.results = res_list
        st.rerun()

with b_col4:
    if st.button("🎲 조합(탱딜힐)", use_container_width=True):
        tank = random.choice(heroes["탱커"])
        dps = random.choice(heroes["딜러"])
        heal = random.choice(heroes["힐러"])
        
        t_role, t_color = get_hero_info("1. 탱커", tank)
        d_role, d_color = get_hero_info("2. 딜러", dps)
        h_role, h_color = get_hero_info("3. 힐러", heal)
        
        st.session_state.results = [
            {"role": t_role, "hero": tank, "color": t_color},
            {"role": d_role, "hero": dps, "color": d_color},
            {"role": h_role, "hero": heal, "color": h_color}
        ]
        st.rerun()
