from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

chat_history = []

SYSTEM_PROMPT = """
You are the Head of Admissions at Chitkara University.

Your job is to answer questions about:
- Admissions
- Eligibility criteria
- Courses and programs
- Fees
- Scholarships
- Campus facilities
- Placements
- Application process

Always answer professionally and clearly.

If you do not know the answer or the information is not provided, say:
'I do not have verified information about that. Please check the official Chitkara University website or contact the admissions office.'

Do not make up information.
"""

def ask_ai(user_text):
    chat_history.append({"role": "user", "content": user_text})
    response = client.chat.completions.create(
        model="google/gemini-2.5-flash-lite",
        messages=[
            {"role" : "system" , "content" : SYSTEM_PROMPT},
            *chat_history 
        ],
        max_tokens=200
    )
    ai_response = response.choices[0].message.content
    chat_history.append({"role": "assistant", "content": ai_response})
    return ai_response

while True:
    user_text = input("You: ")
    reply = ask_ai(user_text)
    print("AI:", reply)
    print(chat_history)
   
