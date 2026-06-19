<!DOCTYPE html>
<html>
<head>
  <title>Random JS Website</title>
  <style>
    body {
      font-family: Arial;
      text-align: center;
      padding-top: 80px;
      transition: 0.3s;
    }

    button {
      padding: 10px 20px;
      font-size: 16px;
      cursor: pointer;
      margin: 10px;
    }
  </style>
</head>

<body>

  <h1 id="title">Welcome 👋</h1>
  <p>Click buttons to see JS in action</p>

  <button onclick="changeColor()">Change Background</button>
  <button onclick="showText()">Show Message</button>

  <script>
    function changeColor() {
      const colors = ["#ffadad", "#ffd6a5", "#fdffb6", "#caffbf", "#9bf6ff", "#a0c4ff"];
      document.body.style.background = colors[Math.floor(Math.random() * colors.length)];
    }

    function showText() {
      const messages = [
        "Hello Developer 🚀",
        "Keep Learning JS 💻",
        "You are doing great 👍",
        "Frontend is fun 🎨"
      ];

      document.getElementById("title").innerText =
        messages[Math.floor(Math.random() * messages.length)];
    }
  </script>

</body>
</html>
