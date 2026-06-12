# 🎯 AI Interview Coach using LangGraph

An AI-powered Interview Coach built using LangGraph and Groq LLM that conducts mock interviews, evaluates answers, analyzes performance, and provides feedback in a continuous interview loop.

## 🚀 Features

* Generates interview questions dynamically
* Accepts user answers
* Evaluates responses using AI
* Calculates performance scores
* Provides personalized feedback
* Adaptive interview flow using LangGraph
* State management using TypedDict
* Graph-based workflow design

---

## 🛠 Technologies Used

* Python
* LangGraph
* LangChain
* Groq LLM
* TypedDict State Management
* Environment Variables (.env)

---

## 📂 Project Structure

```text
Interview_coach/
│
├── main.py          # LangGraph workflow
├── nodes.py         # Interview logic nodes
├── state.py         # State definition
├── .env             # API key (not uploaded)
├── .gitignore
└── README.md
```

---

## 🧠 Workflow

The Interview Coach follows this graph:

```text
Question
    ↓
Answer
    ↓
Evaluate
    ↓
Analyze Performance
    ↓
Feedback
    ↓
Question (Loop)
```

If the user decides to stop:

```text
Answer
   ↓
  END
```

---

## 📄 main.py

The main workflow is created using LangGraph's StateGraph.

Nodes:

* question → Generates interview questions
* answer → Collects user response
* evaluate → Scores the response
* analyze → Calculates overall performance
* feedback → Gives improvement suggestions

Conditional routing:

```python
if state.get("stop"):
    return "end"
```

The interview continues until the user chooses to stop.

---

## 📄 state.py

Defines the InterviewState using TypedDict.

Example state fields:

```python
class InterviewState(TypedDict):
    q: str
    topic: str
    a: str
    score: int
    feedback: str
    avg_score: float
    difficulty: str
    stop: bool
```

Purpose:

* Stores question
* Stores answer
* Stores score
* Tracks performance
* Controls interview flow

---

## 📄 nodes.py

Contains the business logic of the Interview Coach.

Functions:

### ask_question()

Generates a new interview question.

### get_answer()

Collects user response.

### evaluate()

Uses AI to evaluate the answer and assign a score.

### analyze_performance()

Calculates overall performance and difficulty level.

### feedback_node()

Provides personalized feedback and improvement suggestions.

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Lang-Graph-Projects.git
cd Interview_coach
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create .env File

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run Project

```bash
python main.py
```

---

## Sample Interview Flow

```text
Question:
What is Python?

Your Answer:
Python is a high-level programming language.

Score:
8/10

Feedback:
Good explanation. Include examples to improve your answer.

Average Score:
8.0
```

---

## 🎯 Learning Objectives

This project demonstrates:

* LangGraph Fundamentals
* State Management
* Conditional Routing
* AI Evaluation Systems
* Graph-Based Agent Workflows
* Interview Automation

---

## 🔮 Future Improvements

* Difficulty adaptation
* Resume-based interview questions
* Voice interview support
* Performance dashboard
* Question history
* Streamlit Web UI

---

## 👩‍💻 Author

Bhakti Jadhav

Built while learning LangGraph, LangChain, Groq, and AI Agent Development.
