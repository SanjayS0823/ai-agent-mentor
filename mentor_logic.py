from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_llm(prompt):

    messages = [
        {
            "role": "system",
            "content": "You are an expert AI mentor helping university students with career guidance."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        temperature=0.3,
        messages=messages
    )

    return response.choices[0].message.content


def career_guidance(chat_history, question):

    messages = [
        {
            "role": "system",
            "content": "You are an expert AI mentor helping university students."
        }
    ]

    messages.extend(chat_history)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        temperature=0.3,
        messages=messages
    )

    return response.choices[0].message.content


def recommend_courses(field):

    prompt = f"""
Recommend 4 good online courses for learning {field}.
Mention platform names.
"""

    return ask_llm(prompt)


def generate_projects(field):

    prompt = f"""
Give 4 practical project ideas for students learning {field}.
Explain briefly.
"""

    return ask_llm(prompt)


def analyze_resume(resume):

    prompt = f"""
Review this student resume and suggest improvements.

Resume:
{resume}

Give 4 improvement tips.
"""

    return ask_llm(prompt)

def generate_roadmap(profile):

    prompt = f"""
Create a personalized 6-month career roadmap for this student.

Student Profile:
{profile}

The roadmap should include:
Month 1 - foundations
Month 2 - intermediate learning
Month 3 - practical projects
Month 4 - advanced skills
Month 5 - portfolio building
Month 6 - internship/job preparation

Give clear weekly goals and skills to learn.
"""

    return ask_llm(prompt)

def skill_gap_analysis(goal, skills):

    prompt = f"""
A student wants to become a {goal}.

Current skills:
{skills}

Identify:

1. Missing important skills
2. Recommended skills to learn next
3. Suggested learning order
4. Beginner projects to build

Explain clearly for a university student.
"""

    return ask_llm(prompt)