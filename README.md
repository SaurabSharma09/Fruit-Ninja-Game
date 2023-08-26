<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="banner">
    <img src="https://github.com/SaurabSharma09/Fruit-Ninja-Game/blob/main/Preview-image.png" alt="Fruit Ninja Game" width="600">
  </div>

  <h1 class="title">Fruit Ninja Game</h1>
 

  <div class="centered">
    <p class="intro">Welcome to the <strong>Fruit Ninja Game</strong> repository, "Dive into the captivating world of Fruit Ninja Game! Experience the timeless thrill of slicing fruits and dodging bombs in this faithful recreation. Our project aims to deliver a polished gaming encounter with stunning visuals, smooth animations, and an intuitive interface. Contribute and be part of the fun!".</p>
  </div>

  <div class="centered">
    <img src="demo.gif" alt="Gameplay Demo" width="800">
  </div>

  <h2 class="section-title">Table of Contents</h2>
  <ul class="table-of-contents">
    <li><a href="#introduction">Introduction</a></li>
    <li><a href="#objective">Objective</a></li>
    <li><a href="#scope">Scope</a></li>
    <li><a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#contributing">Contributing</a></li>
   
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ul>

  <div id="introduction" class="section">
    <h2 class="section-title">Introduction</h2>
    <p>The <strong>Fruit Ninja Game</strong> is a tribute to the timeless fun of slicing fruits while dodging dangerous bombs. We've meticulously recreated the gameplay to offer you an authentic experience that pays homage to the beloved classic.</p>
  </div>

  <div id="objective" class="section">
    <h2 class="section-title">Objective</h2>
    <p>Our objective is clear: deliver a polished and immersive gaming encounter. Our focus is on creating an environment that seamlessly captures the magic of the original Fruit Ninja game.</p>
  </div>

  <div id="scope" class="section">
    <h2 class="section-title">Scope</h2>
    <p>This project aims to:</p>
    <ul>
      <li>Preserve the essence of Fruit Ninja's gameplay mechanics</li>
      <li>Present visually stunning 3D models for fruits and bombs</li>
      <li>Deliver smooth and captivating animations for fluid gameplay</li>
      <li>Provide an intuitive and user-friendly interface</li>
    </ul>
  </div>

  <div id="getting-started" class="section">
    <h2 class="section-title">Getting Started</h2>
    <div class="subsection">
      <h3 class="subsection-title">Prerequisites</h3>
      <p>Before you begin, ensure you have the following:</p>
      <ul>
        <li>Python 3.7+</li>
        <li>Pygame library</li>
      </ul>
    </div>
    <div class="subsection">
      <h3 class="subsection-title">Installation</h3>
      <ol>
        <li>Clone the repository:</li>
        <pre><code>git clone https://github.com/yourusername/fruit-ninja-game.git</code></pre>
        <li>Install the required dependencies:</li>
        <pre><code>pip install pygame</code></pre>
      </ol>
    </div>
  </div>

  <div id="usage" class="section">
    <h2 class="section-title">Usage</h2>
    <ol>
      <li>Run the game:</li>
      <pre><code>python main.py</code></pre>
      <li>Follow the on-screen instructions to dive into the action.</li>
      <li>Skillfully slice fruits and tactically avoid bombs to secure high scores!</li>
    </ol>
  </div>

  <div id="features" class="section">
    <h2 class="section-title">Features</h2>
    <ul>
      <li>Faithfully recreated Fruit Ninja gameplay</li>
      <li>Exquisite 3D models for fruits and bombs</li>
      <li>Score tracking system to gauge your progress</li>
    </ul>
  </div>

  <div id="contributing" class="section">
    <h2 class="section-title">Contributing</h2>
    <p>We welcome contributions from fellow enthusiasts! To contribute to the <strong>Fruit Ninja Game</strong>, adhere to these steps:</p>
    <ol>
      <li>Fork this repository.</li>
      <li>Create a new branch: <code>git checkout -b feature/your-feature-name</code></li>
      <li>Commit your changes: <code>git commit -m 'Add some feature'</code></li>
      <li>Push to the branch: <code>git push origin feature/your-feature-name</code></li>
      <li>Submit a pull request.</li>
    </ol>
  </div>

  <div id="Contact" class="section">
    <h2 class="section-title">Contact</h2>
    <p>This project is licensed under the MIT License. Refer to the <a href="LICENSE">LICENSE</a> file for details.</p>
  </div>
  <!-- ... Rest of your content ... -->

<div id="contact" class="section">
  <h2 class="section-title">Contact</h2>
  <p>Feel free to get in touch:</p>
  <ul class="contact-list">
    <li><a href="https://github.com/yourusername" target="_blank">GitHub</a></li>
    <li><a href="https://www.linkedin.com/in/yourusername" target="_blank">LinkedIn</a></li>
    <li>Email: <span class="copyable">your@email.com</span> (Click to copy)</li>
  </ul>
</div>

<script>
  const copyableText = document.querySelector('.copyable');
  copyableText.addEventListener('click', () => {
    const textArea = document.createElement('textarea');
    textArea.value = copyableText.textContent;
    document.body.appendChild(textArea);
    textArea.select();
    document.execCommand('copy');
    document.body.removeChild(textArea);
    alert('Email address copied to clipboard!');
  });
</script>

<script src="script.js"></script>
</body>
</html>


  <div id="acknowledgements" class="section">
    <h2 class="section-title">Acknowledgements</h2>
    <ul>
      <li><a href="https://www.pygame.org/">Pygame</a></li>
      <li>Fruit and bomb images sourced from <a href="https://www.google.com/imghp">Google Images</a></li>
    </ul>
  </div>

  <div class="centered">
    <p class="outro">Feel free to get in touch with us for inquiries or feedback. Enjoy the immersive fruit-slicing experience! 🍉🔪</p>
  </div>

 
</body>
</html>
