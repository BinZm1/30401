<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>역할군 선택</title>
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

        .button-container {
            display: flex;
            gap: 15px;
            margin-top: 20px;
        }

        .role-btn {
            padding: 15px 30px;
            font-size: 18px;
            font-weight: bold;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: transform 0.2s, background-color 0.2s;
        }

        .role-btn:hover {
            transform: scale(1.05);
        }

        .tank { background-color: #2b7de9; }  /* 탱커: 파란색 */
        .damage { background-color: #e63946; } /* 딜러: 빨간색 */
        .support { background-color: #2a9d8f; } /* 힐러: 초록색 */

        #result {
            margin-top: 30px;
            font-size: 22px;
            font-weight: bold;
        }
    </style>
</head>
<body>

    <h1>역할군을 선택하세요</h1>

    <div class="button-container">
        <button class="role-btn tank" onclick="selectRole('탱커')">탱커</button>
        <button class="role-btn damage" onclick="selectRole('딜러')">딜러</button>
        <button class="role-btn support" onclick="selectRole('힐러')">힐러</button>
    </div>

    <div id="result"></div>

    <script>
        function selectRole(role) {
            document.getElementById('result').innerText = `선택한 역할군: ${role}`;
        }
    </script>

</body>
</html>
