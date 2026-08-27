import streamlit as st
import random

# 앱 제목
st.title("🎮 오버워치 2 캐릭터 추천기")

# 역할군 선택 버튼 (3열 레이아웃)
col1, col2, col3 = st.columns(3)

with col1:
    tank_selected = st.button("🛡️ 탱커", use_container_width=True)
with col2:
    dealer_selected = st.button("⚔️ 딜러", use_container_width=True)
with col3:
    healer_selected = st.button("➕ 힐러", use_container_width=True)

# 버튼 클릭 상태를 세션 상태(Session State)에 저장
if tank_selected:
    st.session_state["role"] = "탱커"
elif dealer_selected:
    st.session_state["role"] = "딜러"
elif healer_selected:
    st.session_state["role"] = "힐러"

# 오버워치 탱커 영웅 목록
tank_heroes = [
    "D.Va", "둠피스트", "라인하르트", "로드호그", "마우가", 
    "라마트라", "레킹볼", "시그마", "오리사", "윈스턴", "자리야", "정커퀸"
]

# '탱커'가 선택되었을 때 실행할 화면
if st.session_state.get("role") == "탱커":
    st.divider()
    st.subheader("🛡️ 탱커 역할군이 선택되었습니다.")
    
    # 1. 캐릭터 등장 확률 계산 및 안내
    total_tanks = len(tank_heroes)
    probability = round(100 / total_tanks, 2)
    
    st.info(f"현재 등록된 탱커 영웅은 총 **{total_tanks}명**입니다. (개별 뽑기 확률: 약 **{probability}%**)")
    
    # 확률표 접어두기/펼치기
    with st.expander("📊 탱커 캐릭터별 등장 확률 확인하기"):
        # 2열로 나누어 보기 좋게 표시
        p_col1, p_col2 = st.columns(2)
        for i, hero in enumerate(tank_heroes):
            if i % 2 == 0:
                p_col1.write(f"- **{hero}**: {probability}%")
            else:
                p_col2.write(f"- **{hero}**: {probability}%")

    # 2. '선택' 버튼 생성
    if st.button("🎯 탱커 3명 뽑기 (선택)", type="primary", use_container_width=True):
        # 중복 없이 3명 무작위 추첨
        selected_heroes = random.sample(tank_heroes, 3)
        
        st.success("🎉 **추천된 탱커 캐릭터 3명:**")
        
        # 결과를 3개 카드로 나누어 출력
        res_col1, res_col2, res_col3 = st.columns(3)
        with res_col1:
            st.metric(label="1번 영웅", value=selected_heroes[0])
        with res_col2:
            st.metric(label="2번 영웅", value=selected_heroes[1])
        with res_col3:
            st.metric(label="3번 영웅", value=selected_heroes[2])

elif st.session_state.get("role") in ["딜러", "힐러"]:
    st.divider()
    st.warning(f"현재 {st.session_state['role']} 기능은 준비 중입니다. '탱커'를 선택해 주세요!")
