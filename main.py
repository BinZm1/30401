import random
import streamlit as st

# 오버워치 로고 이미지 (PNG)
OW_LOGO_URL = "https://upload.wikimedia.org/wikipedia/commons/5/55/Overwatch_circle_logo.svg"

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
    "라이프위버", "일리아리", "메르시"
]

# 골드색 테두리 (추천함) 영웅 목록
GOLD_HEROES = [
    # 탱커
    "디몬", "시그마", "자리야", "오리사", "마우가",
    # 딜러
    "소전", "파라", "프레야", "엠레", "시온", "안란", "시에라",
    # 힐러
    "키리코", "아나", "젠야타", "우양", "모이라"
]

BROWN_COLOR = "#8B4513"  # 갈색
GOLD_COLOR = "#FFD700"   # 골드색

def get_hero_info(role_name, hero_name):
    """
    영웅 이름을 판별하여 (표시할 역할군/상태 텍스트, 테두리 색상) 튜플을 반환합니다.
    """
    if hero_name in GOLD_HEROES:
        return "⭐ 추천함", GOLD_COLOR
    if hero_name in BROWN_HEROES:
        return "⚠️ 추천안함", BROWN_COLOR
    
    base_role = role_name.split()[0].replace("1.", "").replace("2.", "").replace("3.", "").replace("4.", "").replace("5.", "").strip()
    return role_name, ROLE_COLORS.get(base_role, "#F57C00")

# 페이지 기본 설정
st.set_page_config(page_title="오버워치 영웅 추천", page_icon="🎮", layout="wide")

# CSS 배경 및 레이아웃 수정 (배경만 나타나는 오류 해결)
st.markdown(f"""
    <style>
    /* 기본 앱 배경 */
    .stApp {{
        background-color: #080a0f;
        background-image: 
            radial-gradient(circle at 50% 15%, rgba(245, 124, 0, 0.25) 0%, transparent 60%),
            radial-gradient(circle at 10% 90%, rgba(43, 140, 190, 0.18) 0%, transparent 50%),
            linear-gradient(rgba(255, 255, 255, 0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
        background-size: 100% 100%, 100% 100%, 30px 30px, 30px 30px;
        background-position: 0 0, 0 0, -1px -1px, -1px -1px;
    }}
    
    /* 중앙 오버워치 로고 배경 (워터마크) - 독립 레이어 처리 */
    div[data-testid="stAppViewContainer"]::before {{
        content: "";
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 550px;
        height: 550px;
        background-image: url('{OW_LOGO_URL}');
        background-repeat: no-repeat;
        background-position: center;
        background-size: contain;
        opacity: 0.08;
        filter: drop-shadow(0 0 25px rgba(245, 124, 0, 0.8));
        pointer-events: none;
        z-index: 0;
    }}

    /* Streamlit 메인 콘텐츠 영역이 오버레이 뒤에 묻히지 않도록 정렬 */
    .main .block-container {{
        position: relative;
        z-index: 1;
    }}
    
    /* 타이틀 디자인 */
    .main-title {{
        text-align: center;
        font-family: 'Pretendard', 'Malgun Gothic', 'Noto Sans KR', sans-serif;
        font-weight: 900;
        font-size: 3.3rem;
        letter-spacing: 2px;
        color: #F57C00;
        margin-top: -10px;
        margin-bottom: 5px;
        text-shadow: 0 0 25px rgba(245, 124, 0, 0.7), 2px 2px 10px #000000;
    }}
    
    .sub-title {{
        text-align: center;
        color: #B0B7C6;
        font-size: 1.15rem;
        margin-bottom: 35px;
        text-shadow: 1px 1px 3px #000000;
    }}
    
    /* 결과 카드 스타일 */
    .result-card {{
        background: linear-gradient(135deg, rgba(22, 26, 36, 0.88), rgba(12, 14, 20, 0.95));
        border: 2px solid #F57C00;
        border-radius: 16px;
        padding: 24px 10px;
        text-align: center;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
    }}
    
    .result-card:hover {{
        transform: translateY(-8px);
    }}
    
    .role-badge {{
        font-size: 0.95rem;
        font-weight: 800;
        letter-spacing: 1px;
        margin-bottom: 12px;
    }}
    
    .hero-name {{
        font-size: 1.45rem;
        font-weight: 800;
        color: #FFFFFF;
        word-break: keep-all;
        text-shadow: 0 2px 4px rgba(0,0,0,0.8);
    }}
    </style>
""", unsafe_allow_html=True)

# 한글 헤더 표시
st.markdown('<div class="main-title">오버워치 영웅 추천</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">버튼을 눌러 영웅을 무작위로 뽑아보세요!</div>', unsafe_allow_html=True)

# 초기 세션 상태 설정
if "results" not in st.session_state:
    st.session_state.results = [
        {"role": "READY", "hero": "?", "color": "#F57C00"},
        {"role": "READY", "hero": "?", "color": "#F57C00"},
        {"role": "READY", "hero": "?", "color": "#F57C00"},
        {"role": "READY", "hero": "?", "color": "#F57C00"},
        {"role": "READY", "hero": "?", "color": "#F57C00"}
    ]
if "selected_mode" not in st.session_state:
    st.session_state.selected_mode = None

# 결과 카드 표시
num_cards = len(st.session_state.results)
cols = st.columns(num_cards)

for idx, item in enumerate(st.session_state.results):
    with cols[idx]:
        st.markdown(f"""
            <div class="result-card" style="border-color: {item['color']}; box-shadow: 0 6px 24px {item['color']}33, inset 0 0 12px {item['color']}1A;">
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
        st.session_state.selected_mode = "탱커"
        st.rerun()

with b_col2:
    if st.button("⚔️ 딜러 3명", use_container_width=True):
        picked = random.sample(heroes["딜러"], 3)
        res_list = []
        for i in range(3):
            role_text, color = get_hero_info(f"딜러 {i+1}", picked[i])
            res_list.append({"role": role_text, "hero": picked[i], "color": color})
        st.session_state.results = res_list
        st.session_state.selected_mode = "딜러"
        st.rerun()

with b_col3:
    if st.button("💉 힐러 3명", use_container_width=True):
        picked = random.sample(heroes["힐러"], 3)
        res_list = []
        for i in range(3):
            role_text, color = get_hero_info(f"힐러 {i+1}", picked[i])
            res_list.append({"role": role_text, "hero": picked[i], "color": color})
        st.session_state.results = res_list
        st.session_state.selected_mode = "힐러"
        st.rerun()

with b_col4:
    if st.button("🎲 팀 조합 (1탱 2딜 2힐)", use_container_width=True):
        tank = random.choice(heroes["탱커"])
        dps_list = random.sample(heroes["딜러"], 2)
        heal_list = random.sample(heroes["힐러"], 2)
        
        t_role, t_color = get_hero_info("1. 탱커", tank)
        d1_role, d1_color = get_hero_info("2. 딜러 1", dps_list[0])
        d2_role, d2_color = get_hero_info("3. 딜러 2", dps_list[1])
        h1_role, h1_color = get_hero_info("4. 힐러 1", heal_list[0])
        h2_role, h2_color = get_hero_info("5. 힐러 2", heal_list[1])
        
        st.session_state.results = [
            {"role": t_role, "hero": tank, "color": t_color},
            {"role": d1_role, "hero": dps_list[0], "color": d1_color},
            {"role": d2_role, "hero": d2_color, "hero_name": dps_list[1]}, # 구조 맞춤
            {"role": h1_role, "hero": heal_list[0], "color": h1_color},
            {"role": h2_role, "hero": heal_list[1], "color": h2_color}
        ]
        # 위 항목 오탈자 정정
        st.session_state.results[2] = {"role": d2_role, "hero": dps_list[1], "color": d2_color}
        
        st.session_state.selected_mode = "조합"
        st.rerun()

# 확률표 표시 함수
def show_probability_table(role_key):
    hero_list = heroes[role_key]
    total_count = len(hero_list)
    prob = round(100 / total_count, 2)
    
    st.markdown(f"### 📊 {role_key} 등장 확률표 (총 {total_count}명 / 각각 약 {prob}%)")
    
    table_data = []
    for hero in hero_list:
        status = "보통"
        if hero in GOLD_HEROES:
            status = "⭐ 추천함"
        elif hero in BROWN_HEROES:
            status = "⚠️ 추천안함"
            
        table_data.append({
            "영웅 이름": hero,
            "등장 확률": f"{prob}%",
            "추천 상태": status
        })
    st.dataframe(table_data, use_container_width=True)

# 선택한 모드에 맞춰 동적 확률표 보여주기
if st.session_state.selected_mode in ["탱커", "딜러", "힐러"]:
    mode = st.session_state.selected_mode
    with st.expander(f"📊 {mode} 확률표 보기", expanded=True):
        show_probability_table(mode)

elif st.session_state.selected_mode == "조합":
    with st.expander("📊 팀 조합 확률표 보기 (탱커 / 딜러 / 힐러)", expanded=True):
        tab1, tab2, tab3 = st.tabs(["🛡️ 탱커 확률", "⚔️ 딜러 확률", "💉 힐러 확률"])
        with tab1:
            show_probability_table("탱커")
        with tab2:
            show_probability_table("딜러")
        with tab3:
            show_probability_table("힐러")
