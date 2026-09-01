import streamlit as st
import random

# 페이지 설정 및 제목
st.set_page_config(page_title="오버워치 영웅 추천기", page_icon="🎮")
st.title("🎮 오버워치 캐릭터 추천기")

# 1. 역할군별 영웅 데이터 세팅
HERO_DATA = {
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

# 기본 선택 상태 초기화 (처음 접속 시 미선택)
if "selected_role" not in st.session_state:
    st.session_state["selected_role"] = None

# 역할군 변경 함수 (선택 시 이전 뽑기 결과 삭제)
def change_role(role_name):
    st.session_state["selected_role"] = role_name
    if "picked_heroes" in st.session_state:
        del st.session_state["picked_heroes"]

# 2. 상단 역할군 선택 버튼 (3열 레이아웃)
col1, col2, col3 = st.columns(3)

with col1:
    st.button("🛡️ 탱커", use_container_width=True, on_click=change_role, args=("탱커",))
with col2:
    st.button("⚔️ 딜러", use_container_width=True, on_click=change_role, args=("딜러",))
with col3:
    st.button("➕ 힐러", use_container_width=True, on_click=change_role, args=("힐러",))

current_role = st.session_state["selected_role"]

# 3. 역할군이 선택되어 있는 경우의 화면 출력
if current_role in HERO_DATA:
    st.divider()
    
    # 역할군별 아이콘 설정
    icon = "🛡️" if current_role == "탱커" else ("⚔️" if current_role == "딜러" else "➕")
    st.subheader(f"{icon} {current_role} 역할군")
    
    heroes = HERO_DATA[current_role]
    total_count = len(heroes)
    probability = round(100 / total_count, 2)
    
    # 확률 정보 안내
    st.info(f"현재 등록된 **{current_role}** 영웅은 총 **{total_count}명**입니다. (개별 뽑기 확률: 약 **{probability}%**)")
    
    # 확률표 접어두기/펼치기
    with st.expander(f"📊 {current_role} 캐릭터별 등장 확률 확인하기"):
        p_col1, p_col2 = st.columns(2)
        for i, hero in enumerate(heroes):
            if i % 2 == 0:
                p_col1.write(f"- **{hero}**: {probability}%")
            else:
                p_col2.write(f"- **{hero}**: {probability}%")

    # 캐릭터 3명 뽑기 버튼
    if st.button(f"🎯 {current_role} 3명 뽑기 (선택)", type="primary", use_container_width=True):
        st.session_state["picked_heroes"] = random.sample(heroes, 3)

    # 뽑기 결과가 있는 경우 화면에 표시
    if "picked_heroes" in st.session_state:
        picked = st.session_state["picked_heroes"]
        st.success(f"🎉 **추천된 {current_role} 캐릭터 3명:**")
        
        res_col1, res_col2, res_col3 = st.columns(3)
        with res_col1:
            st.metric(label="1번 영웅", value=picked[0])
        with res_col2:
            st.metric(label="2번 영웅", value=picked[1])
        with res_col3:
            st.metric(label="3번 영웅", value=picked[2])

else:
    st.info("상단의 **탱커 / 딜러 / 힐러** 버튼을 클릭하여 역할군을 선택해 주세요!")
