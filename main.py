import random

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

def main():
    print("=== 오버워치 영웅 랜덤 뽑기 ===")
    print("1: 탱커 | 2: 딜러 | 3: 힐러 | 4: 전체 랜덤")
    
    choice = input("원하는 역할군의 번호를 입력하세요: ").strip()
    
    role_map = {"1": "탱커", "2": "딜러", "3": "힐러"}
    
    if choice in role_map:
        selected_role = role_map[choice]
        picked_hero = random.choice(heroes[selected_role])
        print(f"\n[{selected_role}] 뽑기 결과 ➔ {picked_hero}")
    elif choice == "4":
        all_heroes = heroes["탱커"] + heroes["딜러"] + heroes["힐러"]
        picked_hero = random.choice(all_heroes)
        print(f"\n[전체 랜덤] 뽑기 결과 ➔ {picked_hero}")
    else:
        print("\n올바른 번호를 입력해주세요.")

if __name__ == "__main__":
    main()
