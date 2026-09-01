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

# 기본 선택 상태 초기화
if "selected_role" not in st.session_state:
    st.session_state["selected_role"] = None

# 역할군 변경 함수 (선택 시 이전 뽑기 결과 삭제)
def change_role(role_name):
    st.session_state["selected_role"] = role_name
    if "picked_heroes" in st.session_state:
        del st.session_state["picked_heroes"]

# 2. 상단 역할군 선택 버튼
col1, col2, col3 = st.columns(3)

with col1:
    st.button("🛡️ 탱커", use_container_width=True, on_click=change_role, args=("탱커",))
with col2:
    st.button("⚔️ 딜러", use_container_width=True, on_click=change_role, args=("딜러",))
with col3:
    st.button("➕ 힐러", use_container_width=True, on_click=change_role, args=("힐러",))

current_role = st.session_state["selected_role"]

# 3. 역할군이 선택된 경우 화면 출력
if current_role in HERO_DATA:
    st.divider()
    
    icon = "🛡️" if current_role == "탱커" else ("⚔️" if current_role == "딜러" else "➕")
    st.subheader(f"{icon} {current_role} 역할군")
    
    heroes = HERO_DATA[current_role]
    total_count = len(heroes)
    probability = round(100 / total_count, 2)
    
    st.info(f"현재 등록된 **{current_role}** 영웅은 총 **{total_count}명**입니다. (개별 뽑기 확률: 약 **{probability}%**)")
    
    # 확률표 접어두기/펼치기
    with st.expander(f"📊 {current_role} 캐릭터별 등장 확률 확인하기"):
        p_col1, p_col2 = st.columns(2)
        for i, hero in enumerate(heroes):
            display_name = hero
            # 하트 대상 확인
            if hero in ["일리아리", "라이프위버"]:
                display_name += " ❤️"
            
            if i % 2 == 0:
                p_col1.write(f"- **{display_name}**: {probability}%")
            else:
                p_col2.write(f"- **{display_name}**: {probability}%")

    # 캐릭터 3명 뽑기 버튼
    if st.button(f"🎯 {current_role} 3명 뽑기 (선택)", type="primary", use_container_width=True):
        st.session_state["picked_heroes"] = random.sample(heroes, 3)

    # 뽑기 결과 화면 표시
    if "picked_heroes" in st.session_state:
        picked = st.session_state["picked_heroes"]
        st.success(f"🎉 **추천된 {current_role} 캐릭터 3명:**")
        
        res_cols = st.columns(3)
        
        # 강조 조건 정의
        yellow_border_heroes = ["라인하르트", "로드호그", "정커퀸"]
        brown_border_heroes = ["위도우메이커", "토르비욘"]
        heart_heroes = ["일리아리", "라이프위버"]

        for idx, hero in enumerate(picked):
            with res_cols[idx]:
                display_hero = hero
                # 하트 추가
                if hero in heart_heroes:
                    display_hero = f"{hero} ❤️"
                
                # 테두리 스타일 설정
                border_style = "border: 1px solid #e0e0e0; background-color: #ffffff;" # 기본 스타일
                
                if hero in yellow_border_heroes:
                    border_style = "border: 3px solid #f1c40f; background-color: #fffde7;" # 노란색 테두리
                elif hero in brown_border_heroes:
                    border_style = "border: 3px solid #795548; background-color: #efebe9;" # 갈색 테두리

                # 커스텀 HTML 카드로 출력
                st.markdown(
                    f"""
                    <div style="{border_style} padding: 15px; border-radius: 10px; text-align: center; margin-bottom: 10px;">
                        <p style="margin:0; font-size: 14px; color: #666;">{idx + 1}번 영웅</p>
                        <h3 style="margin:5px 0 0 0; color: #333;">{display_hero}</h3>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

else:
    st.info("상단의 **탱커 / 딜러 / 힐러** 버튼을 클릭하여 역할군을 선택해 주세요!")
