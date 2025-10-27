#hello_ai.py
#Rodolfo Tello
#CSCI 130 - Week 1 Project
#10/26/25

import random
import datetime 

def greeting_agent():

current_hour = datetime.datetime.now().hour 
if current_hour < 12:
    time_period = "morning"
    elif current_hour < 17:
        time_period = "afternoon"
        else:
            time_period = "evening"

name = input("What's your name? ")
greetings = [
    f"Good{time_period},{name}! Welcome to AI class!",
    f"Hello {name}! Hope you're having a great{time_period}!",
    f"Hi {name}! Ready to learn AI this{time_period}?"
]
#select and display random greeting
print(random.choice(greetings))

mood = input("\nHow are you feeling about learning AI?")
if "excited" in mood.lowe() or "good" in mood.lower():
    print("That's wonderful! Your enthusiasm will help you learn!")
elif "nervous" in mood.lower() or"worried" in mood.lower():
    print("DOn't worry! We'll take it step by step.")
else: 
    print(f"Thanks for sharing! Let's make this a great learning experience!")

ai_facts = [
    "Did you know? The term 'Artifical Intelligence' was coined in 1956!",
    "Fun fact: Your smartphone uses AI for face recognition!",
    "AI insight: Netflix uses AI to recommend shows you might like!",
    "Did you know? AI helps doctors detect diseases earlier!"
]

print(f"\n{random.choice(ai_facts)}")
print("\nLet's strt our AI journey together!")

if__name__=="__main__":
    print("=" * 50)
    print("Welcome to CSCI 130: INtroduction to AI")
    print("=" * 50)
    print()
    greeting_agent()
    