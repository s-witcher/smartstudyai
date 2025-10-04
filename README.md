
# 🧠 SmartStudyAI — Your AI-Powered Study Companion

**SmartStudyAI** is an intelligent learning assistant that helps students **actively learn, revise, and retain knowledge** more effectively.  
It ingests your study material — such as research papers, textbooks, or notes — and uses AI to **summarize content**, **generate quizzes**, and **create flashcards**, turning passive reading into **active learning**.  

By generating quizzes and flashcards from the same source material, SmartStudyAI reinforces understanding through **active recall** — a scientifically proven learning strategy that enhances long-term retention and comprehension.

---

## 🎯 Why SmartStudyAI?

Traditional studying often relies on passive review — re-reading notes without testing understanding.  
SmartStudyAI transforms that process into **interactive learning**, automatically creating tailored study aids from your materials.

### 🌟 Benefits
- 🧩 **Summarize efficiently:** Grasp key concepts quickly without reading the entire paper.  
- ❓ **Quiz yourself actively:** Reinforce understanding by answering context-aware questions.  
- 💡 **Revise with flashcards:** Convert essential ideas into Q&A cards for spaced repetition and quick recall.  
- ⚡ **Save time:** Automate the creation of summaries, quizzes, and flashcards in seconds.  

---

## ⚙️ How It Works

1. 📄 **Ingest:** Upload or provide a research paper (`.pdf` or `.txt`).  
2. 🧠 **Process:** SmartStudyAI extracts and analyzes the text using a Large Language Model (LLM).  
3. 🪄 **Generate:** Choose your preferred learning mode:  
   - 📝 **Summary** – Concise overview of the document.  
   - ❓ **Quiz** – Generate thought-provoking questions.  
   - 💡 **Flashcards** – Quick memory prompts for revision.  
4. 🧍‍♂️ **Learn Actively:** Review the generated materials and test your understanding.

---

## 🧩 Key Features

- 🔍 Text ingestion from `.pdf` or `.txt` files  
- 🤖 AI-powered summarization, quiz, and flashcard generation  
- 🧠 Promotes *active recall* and *deep learning* techniques  
- 🔄 Modular architecture for easy expansion and custom providers  
- 🌐 Powered by **DigitalOcean Inference API** (`openai-gpt-oss-120b`)  
- 💬 Simple command-line interface (CLI) for quick use  

---

## 🛠️ Tech Stack

| Component | Technology |
|------------|-------------|
| **Language** | Python |
| **Core Libraries** | `requests`, `PyPDF2` |
| **LLM Provider** | DigitalOcean Inference API |
| **Architecture** | Modular (Ingestion, Provider, Algorithms, CLI Interface) |

---

## 🚀 Example Workflow

```bash
$ python main.py
=== SmartStudyAI ===
Enter path to research paper (.pdf or .txt): sample_paper.pdf
Choose task (summary/quiz/flashcards): quiz
```

📘 **Output Example:**
```
Q1: What was the main objective of the research study?
Q2: Which methods were used to validate the results?
Q3: What key conclusion did the authors reach?
```

---

## 🧠 Active Learning Philosophy

SmartStudyAI is designed around **active recall** and **retrieval practice** — powerful learning strategies that involve recalling information from memory rather than passively reviewing it.  
By generating quizzes and flashcards from your own study material, SmartStudyAI helps you:
- Strengthen neural connections through repeated recall  
- Identify weak areas for improvement  
- Turn revision into an engaging and adaptive experience  

---

## 🔮 Future Enhancements

SmartStudyAI is built with scalability and personalized learning in mind.  
Here are some exciting features planned for future releases:

- 🧠 **Adaptive Question Memory:**  
  Remembers previously asked questions for each document and generates new, more challenging ones to encourage continuous learning without repetition.

- 🧾 **Custom Diagrams & Visual Summaries:**  
  Automatically create concept maps, flow diagrams, and key-point visuals to improve comprehension of complex topics.

- ✅ **Intelligent Checklists:**  
  Generate dynamic checklists based on key topics, helping students track progress and completion of learning goals.

- 📈 **Progress Tracking Dashboard:**  
  Monitor study patterns, quiz performance, and content coverage through an interactive analytics interface.

- 🏆 **Gamified Reward System:**  
  Introduce badges, XP points, and streaks to motivate consistent study habits and make learning more engaging.

- 🔄 **Session Continuity & History:**  
  Store previous study sessions and materials so students can resume learning, review past quizzes, and measure growth over time.

---

## 🌱 Vision

SmartStudyAI aims to evolve into a **personalized learning ecosystem** — combining AI-driven summarization, adaptive testing, and gamification to make studying both effective and enjoyable.

> **"Don’t just read — recall, revise, and retain with SmartStudyAI."**

---

## 📬 Author & Contributions

Created as part of an AI-based educational tool initiative to enhance **active learning through automation**.  
Contributions, feedback, and feature ideas are always welcome!

---

## 🧩 Project Structure

```
smartstudyai/
├── README.md
├── main.py
├── ingestion/
│   └── file_ingestion.py
├── providers/
│   ├── llm_provider.py
│   └── doai_provider.py
└── algorithms/
    ├── summarizer.py
    ├── quiz_generator.py
    └── flashcard_creator.py
```

---

## ⚙️ Setup & Usage

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set your API key**
   ```bash
   export DOAI_API_KEY="your_digitalocean_model_key"
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

---

**SmartStudyAI — Learn actively, recall deeply, and study smarter.**
