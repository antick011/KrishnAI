# 🕉️ KrishnaAI – Divine Chatbot of Lord Krishna

**KrishnaAI** is an intelligent single-page spiritual assistant inspired by the teachings of *Lord Krishna*. It uses emotion detection to provide Bhagavad Gita verses and divine guidance tailored to the user’s feelings — in English, Hindi, or Bengali.

Built using **Python (Flask)** for the backend and **HTML, CSS, JS + Bootstrap** for the frontend, it creates a calming, immersive experience enhanced by **continuous Om chanting** in the background.

---

## 🌟 Features

### 🔮 Emotion-Based Intelligence
- Analyzes user queries using keyword-based emotion detection.
- Maps emotional states like *grief*, *hope*, *confusion*, *desire*, etc. to relevant Gita verses.

### 🕉️ Divine Bhagavad Gita Responses
- Displays:
  - **Detected Emotion**
  - **Sanskrit Shloka**
  - **Translation**
  - **Krishna’s Divine Message** (custom text)

### 🌐 Multi-language Support
- Supports **English (en)**, **Hindi (hi)**, and **Bengali (bn)** input and output.
- Automatically selects translated divine messages based on language choice.

### 🎧 Continuous Om Chanting
- Plays a looping “Om” sound in the background for meditative atmosphere.
- Begins automatically when the page loads.

### 💻 Modern UI/UX (Single Page)
- Fully responsive design using **Bootstrap 5**.
- Floating animated Krishna image.
- Beautiful dark theme with glowing accents.
- No scrolling — all features fit within a single view.

---

## 🛠️ Tech Stack

| Layer     | Tech Used                     |
|-----------|-------------------------------|
| Frontend  | HTML5, CSS3, JavaScript, Bootstrap 5 |
| Backend   | Python 3.x, Flask             |
| AI Logic  | Custom NLP-based emotion detection (`model.py`) |
| Assets    | Sanskrit verses JSON, Om audio, Krishna PNG |

---

## 🧪 How It Works

1. **User types a message** expressing their thoughts or emotions.
2. Backend uses keyword mapping in `model.py` to **detect emotion**.
3. Fetches matching Gita verse from the dataset (`krishna_dataset.json`).
4. Responds with the full **emotional analysis + verse + message**.
5. **Om sound** plays throughout for immersive spirituality.

---

## 📁 Folder Structure

KrishnaAI/
├── app.py
├── model.py
├── krishna_dataset.json
├── requirements.txt
├── static/
│ ├── css/style.css
│ ├── js/main.js
│ ├── audio/om.mp3
│ └── images/krishn.png
└── templates/
└── index.html


---

## 👨‍💻 Developer

Built with devotion by **Antick Roy**  
*Corporate Trainer • Explorer • AI Developer • Spiritual Tech Creator*

---

## 🙏 License

This project is open-source and available for educational and spiritual use. Commercial use is not permitted without permission.

---

## 🧘‍♂️ Final Words

Let Krishna guide you through code, consciousness, and clarity.

> “Whenever dharma declines and the purpose of life is forgotten, I manifest myself.”  
> — *Bhagavad Gita 4.7*

