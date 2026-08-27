import streamlit as st  # Streamlit을 사용하는 경우

# HTML/CSS 코드를 문자열(""" """)로 감싸서 변수에 저장
html_code = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            background-color: #f4f4f9;
        }
        .button-container { display: flex; gap: 15px; margin-top: 20px; }
        .role-btn {
            padding: 15px 30px;
            font-size: 18px;
            font-weight: bold;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }
        .tank { background-color: #2b7de9; }
        .damage { background-color: #e63946; }
        .support { background-color: #2a9d8f; }
    </style>
</head>
<body>
    <h1>역할군을 선택하세요</h1>
    <div class="button-container">
        <button class="role-btn tank" onclick="alert('탱커 선택')">탱커</button>
        <button class="role-btn damage" onclick="alert('딜러 선택')">딜러</button>
        <button class="role-btn support" onclick="alert('힐러 선택')">힐러</button>
    </div>
</body>
</html>
"""

# Streamlit에서 HTML 출력하기
st.components.v1.html(html_code, height=600)
