from groq import Groq               # connects to model API
from dotenv import load_dotenv      # Loads API key from .env file
import os, json
from datetime import datetime

# Files to store data
MEM = "memory.json"
ANA = "analysis.json"


# LOAD DATA 
def load_file(f):
    if not os.path.exists(f):
        return []
    try:
        with open(f) as file:
            return json.load(file)
    except:
        return []


# SAVE DATA 
def save_file(f, data):
    with open(f, "w") as file:
        json.dump(data, file, indent=2)


# Load API key
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# CALL AI 
def llm(prompt):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


#  ASK QUESTION 
def ask_question(state):
    question = llm("Generate ONE aptitude question (Math, Logic, English).")
    print("\nQuestion:\n", question)
    return {"q": question}


# GET ANSWER 
def get_answer(state):
    answer = input("\nYour Answer (type exit to stop): ")

    if answer.lower() in ["exit", "quit", "stop"]:
        return {"stop": True}

    return {"a": answer, "stop": False}


# EVALUATE ANSWER
def evaluate(state):

    result = llm(f"""
Question: {state['q']}
Answer: {state['a']}

Give:
CORRECTNESS
CORRECT_ANSWER
EXPLANATION
SCORE (0-10)
FEEDBACK
""")

    # Extract score
    score = 0
    for line in result.split("\n"):
        if "SCORE:" in line:
            try:
                score = int(line.split(":")[1].strip())
            except:
                score = 0
            break

    # Save full history
    memory = load_file(MEM)
    memory.append({
        "time": str(datetime.now()),
        "question": state["q"],
        "answer": state["a"],
        "score": score,
        "feedback": result
    })
    save_file(MEM, memory)

    # Save only scores
    analysis = load_file(ANA)
    analysis.append({
        "time": str(datetime.now()),
        "score": score
    })
    save_file(ANA, analysis)

    return {"feedback": result, "score": score}


# AVERAGE SCORE 
def analyze_performance(state):
    scores = [i["score"] for i in load_file(ANA)]
    avg = sum(scores) / len(scores) if scores else 0
    return {"avg_score": round(avg, 2)}


# SHOW RESULT
def feedback_node(state):

    print("\n====================")

    print("Question Result:")
    print(state["feedback"])

    print("\nScore:", state["score"])
    print("Average Score:", state["avg_score"])

    print("====================")

    return {}