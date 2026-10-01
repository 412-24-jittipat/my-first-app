<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>เกมทายชื่อสัตว์</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #74ebd5, #ACB6E5);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .game {
            width: 90%;
            max-width: 600px;
            background: white;
            padding: 30px;
            border-radius: 20px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }

        h1 {
            color: #333;
            margin-bottom: 10px;
        }

        .score {
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 20px;
            color: #555;
        }

        #animalImage {
            width: 100%;
            max-width: 450px;
            height: 280px;
            object-fit: cover;
            border-radius: 15px;
            margin-bottom: 20px;
            background: #eee;
        }

        .question {
            font-size: 22px;
            font-weight: bold;
            margin-bottom: 15px;
        }

        input {
            width: 80%;
            padding: 12px;
            font-size: 18px;
            border: 2px solid #ddd;
            border-radius: 10px;
            outline: none;
            text-align: center;
        }

        input:focus {
            border-color: #74ebd5;
        }

        button {
            margin-top: 15px;
            padding: 12px 25px;
            font-size: 18px;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            background: #4CAF50;
            color: white;
        }

        button:hover {
            background: #3d9140;
        }

        #result {
            margin-top: 15px;
            font-size: 18px;
            font-weight: bold;
            min-height: 25px;
        }

        #nextButton {
            background: #2196F3;
            display: none;
        }

        #nextButton:hover {
            background: #1976D2;
        }

        #restartButton {
            background: #ff9800;
            display: none;
        }

        #restartButton:hover {
            background: #e68900;
        }
    </style>
</head>

<body>

<div class="game">

    <h1>🐾 เกมทายชื่อสัตว์ 🐾</h1>

    <div class="score">
        ข้อที่ <span id="questionNumber">1</span> / 6
        <br>
        คะแนน: <span id="score">0</span>
    </div>

    <img id="animalImage" src="" alt="ภาพสัตว์">

    <div class="question">
        สัตว์ในภาพคืออะไร?
    </div>

    <input
        type="text"
        id="answer"
        placeholder="พิมพ์ชื่อสัตว์"
    >

    <br>

    <button id="checkButton" onclick="checkAnswer()">
        ทายคำตอบ
    </button>

    <div id="result"></div>

    <button id="nextButton" onclick="nextQuestion()">
        ข้อถัดไป
    </button>

    <button id="restartButton" onclick="restartGame()">
        เล่นอีกครั้ง
    </button>

</div>


<script>

    // ข้อมูลสัตว์ทั้ง 6 ข้อ
    const animals = [
        {
            image: "images/dog.jpg",
            answer: "สุนัข"
        },
        {
            image: "images/cat.jpg",
            answer: "แมว"
        },
        {
            image: "images/elephant.jpg",
            answer: "ช้าง"
        },
        {
            image: "images/lion.jpg",
            answer: "สิงโต"
        },
        {
            image: "images/panda.jpg",
            answer: "แพนด้า"
        },
        {
            image: "images/tiger.jpg",
            answer: "เสือ"
        }
    ];

    let currentQuestion = 0;
    let score = 0;


    // แสดงคำถาม
    function showQuestion() {

        document.getElementById("animalImage").src =
            animals[currentQuestion].image;

        document.getElementById("questionNumber").textContent =
            currentQuestion + 1;

        document.getElementById("score").textContent =
            score;

        document.getElementById("answer").value = "";

        document.getElementById("result").textContent = "";

        document.getElementById("checkButton").style.display =
            "inline-block";

        document.getElementById("nextButton").style.display =
            "none";

        document.getElementById("answer").disabled = false;
    }


    // ตรวจคำตอบ
    function checkAnswer() {

        const userAnswer =
            document.getElementById("answer").value.trim();

        const correctAnswer =
            animals[currentQuestion].answer;

        if (userAnswer === "") {
            document.getElementById("result").textContent =
                "กรุณาพิมพ์คำตอบก่อนนะ";
            return;
        }

        if (userAnswer === correctAnswer) {

            score++;

            document.getElementById("result").textContent =
                "✅ ถูกต้อง!";

        } else {

            document.getElementById("result").textContent =
                "❌ ผิด! คำตอบคือ " + correctAnswer;
        }

        document.getElementById("score").textContent = score;

        document.getElementById("checkButton").style.display =
            "none";

        document.getElementById("answer").disabled = true;

        if (currentQuestion < animals.length - 1) {

            document.getElementById("nextButton").style.display =
                "inline-block";

        } else {

            showFinalScore();
        }
    }


    // ไปข้อถัดไป
    function nextQuestion() {

        currentQuestion++;

        showQuestion();
    }


    // แสดงคะแนนสุดท้าย
    function showFinalScore() {

        document.getElementById("question").style.display =
            "none";

        document.getElementById("nextButton").style.display =
            "none";

        document.getElementById("restartButton").style.display =
            "inline-block";

        document.getElementById("result").textContent =
            "🎉 จบเกม! คุณได้ " + score + " / 6 คะแนน";
    }


    // เริ่มเกมใหม่
    function restartGame() {

        currentQuestion = 0;
        score = 0;

        document.getElementById("restartButton").style.display =
            "none";

        document.getElementById("answer").disabled = false;

        showQuestion();
    }


    // เริ่มเกม
    showQuestion();

</script>

</body>
</html>
