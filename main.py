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

# 기본 역할군 색상
ROLE_COLORS = {
    "탱커": "#2B8CBE",  # 파란색
    "딜러": "#E65100",  # 주황색
    "힐러": "#2E7D32"   # 초록색
}

# 갈색 테두리를 적용할 영웅 목록
BROWN_HEROES = [
    # 탱커
    "로드호그", "라인하르트", "둠피스트", "정커퀸",
    # 딜러
    "위도우메이커", "캐서디", "토르비욘",
    # 힐러
    "라이프위버", "일리아리", "모이라"
]

BROWN_COLOR = "#8B4513"  # 갈색 (SaddleBrown)

def get_hero_color(role, hero_name):
    """지정된 특수 영웅이면 갈색, 아니면 기본 역할군 색상을 반환합니다."""
    if hero_name in BROWN_HEROES:
        return BROWN_COLOR
    return ROLE_COLORS.get(role, "#F57C00")

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
    
    /* 결과 카드 컨테이너 */
    .result-container {
        display: flex;
        gap: 15px;
        justify-content: center;
        margin-bottom: 30px;
    }
    
    .result-card {
        flex: 1;
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
        st.session_state.results = [
            {"role": "탱커 1", "hero": picked[0], "color": get_hero_color("탱커", picked[0])},
            {"role": "탱커 2", "hero": picked[1], "color": get_hero_color("탱커", picked[1])},
            {"role": "탱커 3", "hero": picked[2], "color": get_hero_color("탱커", picked[2])}
        ]
        st.rerun()

with b_col2:
    if st.button("⚔️ 딜러 3명", use_container_width=True):
        picked = random.sample(heroes["딜러"], 3)
        st.session_state.results = [
            {"role": "딜러 1", "hero": picked[0], "color": get_hero_color("딜러", picked[0])},
            {"role": "딜러 2", "hero": picked[1], "color": get_hero_color("딜러", picked[1])},
            {"role": "딜러 3", "hero": picked[2], "color": get_hero_color("딜러", picked[2])}
        ]
        st.rerun()

with b_col3:
    if st.button("💉 힐러 3명", use_container_width=True):
        picked = random.sample(heroes["힐러"], 3)
        st.session_state.results = [
            {"role": "힐러 1", "hero": picked[0], "color": get_hero_color("힐러", picked[0])},
            {"role": "힐러 2", "hero": picked[1], "color": get_hero_color("힐러", picked[1])},
            {"role": "힐러 3", "hero": picked[2], "color": get_hero_color("힐러", picked[2])}
        ]
        st.rerun()

with b_col4:
    if st.button("🎲 조합(탱딜힐)", use_container_width=True):
        tank = random.choice(heroes["탱커"])
        dps = random.choice(heroes["딜러"])
        heal = random.choice(heroes["힐러"])
        st.session_state.results = [
            {"role": "1. 탱커", "hero": tank, "color": get_hero_color("탱커", tank)},
            {"role": "2. 딜러", "hero": dps, "color": get_hero_color("딜러", dps)},
            {"role": "3. 힐러", "hero": heal, "color": get_hero_color("힐러", heal)}
        ]
        st.rerun()
