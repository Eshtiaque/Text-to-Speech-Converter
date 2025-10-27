# 🗣️ Instant Text-to-Speech Generator (Streamlit & gTTS)

A modern, mobile-friendly web application for converting plain text or uploaded `.txt` files into downloadable MP3 audio. Powered by **Streamlit** and **gTTS (Google Text-to-Speech)**. Optimized for a wide, single-screen experience.

---

## 🚀 Quick Setup & Local Run

Follow these steps to run the app on your computer.

### Prerequisites

- Python 3.7 or later must be installed.

### Project Structure

Make sure your project folder includes these files:

- `app.py` – main application code
- `requirements.txt` – required library list

#### `requirements.txt` contents
streamlit
gTTS

---

### ⚙️ Environment Setup

Open your terminal/command prompt, navigate to the project directory, and run:

#### Windows (Command Prompt/PowerShell)
```
python -m venv venv
.\venv\Scripts\activate
```

#### macOS/Linux
python3 -m venv venv
source venv/bin/activate

text

---

### 📦 Install Dependencies

Install the needed libraries:
```
pip install streamlit gtts
```

---

### ▶️ Run the Application

Start the Streamlit development server:
```
python -m streamlit run app.py
```

Your browser should open at [http://localhost:8501](http://localhost:8501).

---

## 💻 Features

- Convert entered text or `.txt` file input to downloadable MP3 audio
- Supports all major languages via gTTS
- Fast, simple, responsive single-page UI

---

## 📝 Usage Notes

- Uploaded `.txt` file should be UTF-8 encoded for best compatibility
- gTTS requires an active internet connection
- Download the generated MP3 instantly from the app

---