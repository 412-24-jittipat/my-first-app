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
}

.score {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 20px;
}

#animalImage {
    width: 100%;
    height: 300px;
    object-fit: cover;
    border-radius: 15px;
    margin-bottom: 20px;
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
    text-align: center;
}

button {
    margin: 10px 5px;
    padding: 12px 25px;
    font-size: 18px;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    color: white;
    background: #4CAF50;
}

button:hover {
    opacity: 0.85;
}

#nextButton {
    background: #2196F3;
    display: none;
}

#restartButton {
    background: #ff9800;
    display: none;
}

#result {
    margin-top: 15px;
    font-size: 20px;
    font-weight: bold;
    min-height: 30px;
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

const animals = [

    {
        image: "https://commons.wikimedia.org/wiki/Special:FilePath/16-year-old%20American%20Cocker%20Spaniel%2C%20Rascal%20Dmitri%2C%20at%20sunset.jpg",
        answer: "สุนัข"
    },

    {
        image: "https://commons.wikimedia.org/wiki/Special:FilePath/A%20cat%20expresses%20her%20love.jpg",
        answer: "แมว"
    },

    {
        image: "https://commons.wikimedia.org/wiki/Special:FilePath/Elephant%20near%20Amboseli%20National%20Park.jpg",
        answer: "ช้าง"
    },

    {
        image: "https://commons.wikimedia.org/wiki/Special:FilePath/Lion%20waiting%20in%20Namibia.jpg",
        answer: "สิงโต"
    },

    {
        image: "https://commons.wikimedia.org/wiki/Special:FilePath/Giant%20Panda%20in%20Bifengxia.jpg",
        answer: "แพนด้า"
    },

    {
        image: "https://commons.wikimedia.org/wiki/Special:FilePath/Siberian%20Tiger%20in%20the%20snow.jpg",
        answer: "เสือ"
    }

];

let currentQuestion = 0;
let score = 0;

function showQuestion() {

    document.getElementById("animalImage").src =
        animals[currentQuestion].image;

    document.getElementById("questionNumber").textContent =
        currentQuestion + 1;

    document.getElementById("score").textContent =
        score;

    document.getElementById("answer").value = "";

    document.getElementById("answer").disabled = false;

    document.getElementById("result").textContent = "";

    document.getElementById("checkButton").style.display =
        "inline-block";

    document.getElementById("nextButton").style.display =
        "none";
}

function checkAnswer() {

    const userAnswer =
        document.getElementById("answer").value.trim();

    const correctAnswer =
        animals[currentQuestion].answer;

    if (userAnswer === "") {
        document.getElementById("result").textContent =
            "⚠️ กรุณาพิมพ์คำตอบก่อน";
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

    document.getElementById("answer").disabled = true;

    document.getElementById("checkButton").style.display =
        "none";

    if (currentQuestion < animals.length - 1) {

        document.getElementById("nextButton").style.display =
            "inline-block";

    } else {

        document.getElementById("result").textContent +=
            " 🎉 จบเกม! ได้ " + score + " / 6 คะแนน";

        document.getElementById("restartButton").style.display =
            "inline-block";
    }
}

function nextQuestion() {

    currentQuestion++;

    showQuestion();
}

function restartGame() {

    currentQuestion = 0;
    score = 0;

    document.getElementById("restartButton").style.display =
        "none";

    showQuestion();
}

showQuestion();

</script>

</body>
</html>
