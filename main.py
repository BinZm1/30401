import random
import tkinter as tk

# 역할군별 캐릭터 목록
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

# 역할군별 상징 색상
ROLE_COLORS = {
    "탱커": "#2B8CBE",  # 푸른색
    "딜러": "#E65100",  # 주황색
    "힐러": "#2E7D32",  # 초록색
    "전체": "#F57C00"   # 오버워치 시그니처 주황
}

class OverwatchPickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OVERWATCH 2 - HERO PICKER")
        self.root.geometry("480x560")
        self.root.resizable(False, False)

        # 캔버스 배경 설정 (패턴 구현)
        self.canvas = tk.Canvas(self.root, width=480, height=560, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.draw_background()
        self.setup_ui()

    def draw_background(self):
        """다크 테마 오버워치 스타일 배경 및 스트라이프 디자인"""
        # 어두운 기본 배경 (Hex: #1A1C23)
        self.canvas.create_rectangle(0, 0, 480, 560, fill="#1A1C23", outline="")

        # 사선 스트라이프 디자인 패턴 추가
        for i in range(-200, 600, 24):
            self.canvas.create_line(i, 0, i + 300, 560, fill="#232630", width=6)

        # 상단 타이틀 영문 상징 라인
        self.canvas.create_rectangle(0, 0, 480, 6, fill="#F57C00", outline="")
        
        # 결과 표시 패널 디스플레이 박스 (테두리 글로우 효과)
        self.canvas.create_rectangle(38, 128, 442, 272, fill="#F57C00", outline="") # 외각 글로우
        self.canvas.create_rectangle(40, 130, 440, 270, fill="#0F1015", outline="") # 내부 상자

    def setup_ui(self):
        """UI 엘리먼트 배치"""
        # 타이틀
        title_label = tk.Label(
            self.root, text="OVERWATCH HERO SELECT", 
            font=("Impact", 22), fg="#FFFFFF", bg="#1A1C23"
        )
        title_label.place(x=240, y=40, anchor="center")

        sub_label = tk.Label(
            self.root, text="영웅을 선택하세요", 
            font=("맑은 고딕", 10, "bold"), fg="#8A8F9E", bg="#1A1C23"
        )
        sub_label.place(x=240, y=75, anchor="center")

        # 결과 출력 라벨 (역할군 / 영웅 이름)
        self.role_label = tk.Label(
            self.root, text="READY TO PICK", 
            font=("Impact", 14), fg="#F57C00", bg="#0F1015"
        )
        self.role_label.place(x=240, y=165, anchor="center")

        self.result_label = tk.Label(
            self.root, text="?", 
            font=("맑은 고딕", 32, "bold"), fg="#FFFFFF", bg="#0F1015"
        )
        self.result_label.place(x=240, y=215, anchor="center")

        # 버튼 생성 함수 호출
        self.create_button("탱커", "#2B8CBE", 320)
        self.create_button("딜러", "#D84315", 375)
        self.create_button("힐러", "#2E7D32", 430)
        self.create_button("전체 랜덤", "#546E7A", 485, is_all=True)

    def create_button(self, text, color, y_pos, is_all=False):
        """커스텀 호버 효과를 포함한 버튼 생성"""
        btn = tk.Button(
            self.root, text=text, font=("맑은 고딕", 12, "bold"),
            fg="#FFFFFF", bg=color, activeforeground="#FFFFFF", activebackground="#1A1C23",
            relief="flat", cursor="hand2",
            command=lambda: self.pick_hero(text if not is_all else "전체")
        )
        btn.place(x=240, y=y_pos, width=380, height=44, anchor="center")

    def pick_hero(self, role):
        """랜덤 추첨 로직"""
        if role == "전체":
            all_list = heroes["탱커"] + heroes["딜러"] + heroes["힐러"]
            selected_hero = random.choice(all_list)
            # 캐릭터가 속한 실제 역할군 찾기
            for r, h_list in heroes.items():
                if selected_hero in h_list:
                    actual_role = r
                    break
            self.role_label.config(text=f"[ {actual_role} ]", fg=ROLE_COLORS[actual_role])
        else:
            selected_hero = random.choice(heroes[role])
            self.role_label.config(text=f"[ {role} ]", fg=ROLE_COLORS[role])

        self.result_label.config(text=selected_hero)

if __name__ == "__main__":
    root = tk.Tk()
    app = OverwatchPickerApp(root)
    root.mainloop()
