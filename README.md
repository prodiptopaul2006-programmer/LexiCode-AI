# 🚀 LexiCode AI

> Transform messy code snippets into crystal-clear documentation, plain-English explanations, and logic breakdowns instantly using state-of-the-art AI.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0.2-green?style=flat-square&logo=flask&logoColor=white)
![Groq API](https://img.shields.io/badge/AI-Groq%20(GPT%20OSS)-orange?style=flat-square&logo=openai&logoColor=white)
![Security](https://img.shields.io/badge/Security-Hardened-critical?style=flat-square&logo=security&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-purple?style=flat-square)


## ✨ Key Features

* **🧠 Instant AI Documentation**: Automatically parses code snippets and generates professional documentation, explanations, and step-by-step logic breakdowns.
* **⚡ High-Performance Inference**: Powered by Groq's high-speed inference engine using the `openai/gpt-oss-120b` model.
* **🎨 Modern Responsive UI**: Built with a sleek, dark-mode interface styled via Tailwind CSS.
* **🛡️ Production-Grade Security**: 
  * **IP-Based Rate Limiting** (`Flask-Limiter`) to prevent API abuse and DoS attempts.
  * **Strict Input Validation** with length constraints (capped at 5,000 characters) to mitigate token exhaustion and memory overload.
  * **Secure Server-Side Logging** with sanitized generic error responses to prevent internal stack trace leaks.



## 🏗️ Architecture & Tech Stack

* **Backend**: Python, Flask, Groq SDK, Flask-Limiter
* **Frontend**: HTML5, Tailwind CSS (via CDN), Vanilla JavaScript (`fetch` API)
* **Security & Environment**: Environment-variable credential isolation (`os.environ`), structured Python logging

## ⚙️ Getting Started & Installation

Follow these steps to set up and run LexiCode-AI locally on your machine.

### 1. Clone or Download the Repository
If you have Git installed, clone the repository:
bash
git clone [https://github.com/prodiptopaul2006-programmer/LexiCode-AI.git](https://github.com/prodiptopaul2006-programmer/LexiCode-AI.git)
cd LexiCode-AI
(Or download the ZIP archive directly from GitHub and extract it to your local directory).

2. Install Dependencies
Make sure you have Python installed, then install the required packages:

Bash
pip install -r requirements.txt
3. Configure Your Environment Variable
Set your Groq API key in your terminal session before running the application:

On Windows (PowerShell):

PowerShell
$env:GROQ_API_KEY="your_actual_groq_api_key_here"
On macOS / Linux (Terminal):

Bash
export GROQ_API_KEY="your_actual_groq_api_key_here"
4. Run the Application
Start the Flask development server:

Bash
python app.py
Open your browser and navigate to:
👉 http://127.0.0.1:5000

🔒 Security Practices Built-In
LexiCode-AI is designed with defensive programming and cybersecurity best practices in mind:

API Key Protection: Secrets are never hardcoded; they rely strictly on environment variables and are excluded from version control via .gitignore.

Abate Scraping & Spam: The /generate endpoint enforces a strict rate limit per client IP address.

Safe DOM Rendering: Frontend code uses text nodes (innerText) rather than raw HTML injection, neutralizing DOM-based XSS vulnerabilities.

🤝 Contributing
Contributions, feature suggestions, and security audits are welcome! Feel free to fork this repository, open an issue, or submit a pull request.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License
Distributed under the MIT License. See LICENSE for more information.
