# 🤖 Jarvis – Personal AI Assistant (Python)

Jarvis is a **Python-based personal AI assistant** that interacts with users via text commands and performs real-world tasks such as opening applications, searching the web, playing YouTube videos, fetching weather information, performing calculations, and more.

This project demonstrates **Python fundamentals, automation, API usage, and logical problem-solving**, making it suitable for entry-level roles and learning purposes.

---

## 🚀 Features

- 🕒 Tells current time and date (including yesterday & tomorrow)
- 🌐 Opens websites (Google, YouTube, GitHub, etc.)
- 🖥 Opens desktop applications (VS Code, MS Word, Excel, Power BI, browsers, etc.)
- ▶ Plays videos directly on YouTube
- 📚 Searches topics using Wikipedia with fallback to Google
- 🧮 Performs mathematical calculations using natural language
- 🌦 Fetches real-time weather information
- 🔄 Handles invalid inputs gracefully
- ❌ Supports exit/quit commands

---

## 🛠 Technologies & Libraries Used

- **Python 3**
- `datetime`
- `webbrowser`
- `os`
- `math`
- `subprocess`
- `pywhatkit`
- `wikipedia`
- `requests`
- `beautifulsoup4`

---

## 📂 Project Structure

Jarvis-Personal-AI-Assistant/
│
├── Main.py # Main Python file containing Jarvis logic
├── README.md # Project documentation
├── requirements.txt # Required Python libraries
├── .gitignore # Files/folders to ignore in Git


---

## ⚙ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/TushalMehra/Jarvis-Personal-AI-Assistant.git

2️⃣ Navigate to the project folder
```bash

cd Jarvis-Personal-AI-Assistant

3️⃣ Install required dependencies

pip install -r requirements.txt

4️⃣ Run the program

python Main.py

---

## Example Commands

What is the time?
Open Instagram
Play shape of you
Search Python programming
What is machine learning?
Calculate 45 * 12
Weather in Delhi
Open VS Code
Exit


## How It Works 

Takes user input in a loop

Matches keywords using conditional logic

Executes actions using Python standard libraries and APIs

Uses Wikipedia API for summaries

Uses web scraping for weather information

Opens applications and websites using OS-level commands


🔮 Future Improvements

Add voice recognition

Convert to GUI-based assistant

Add chatbot/LLM integration

Improve NLP handling

Cross-platform support

👤 Author

Tushal Mehra
Aspiring Data Analyst | Python | SQL | Power BI

📌 GitHub: https://github.com/TushalMehra
