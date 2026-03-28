# 🎓 AI Mentor Agent

## Overview

AI Mentor Agent is an AI-powered web application that provides career guidance to students.
The system acts as a virtual mentor that helps users explore career paths, identify skill gaps, discover learning resources, and build a structured roadmap toward their career goals.

The application uses a **Large Language Model (LLM)** to generate intelligent responses for various student queries related to career development.

---

## Features

### 💬 Career Chat Mentor

Students can interact with an AI mentor to ask career-related questions such as:

* How to become a Machine Learning Engineer
* What skills are required for Data Science
* How to prepare for internships

The AI provides structured career advice.

---

### 📚 Course Recommendations

The system suggests relevant online courses based on a selected career field.

Example fields:

* Artificial Intelligence
* Data Science
* Web Development
* Cybersecurity
* Cloud Computing

---

### 💡 Project Idea Generator

Generates practical project ideas for students based on their selected field of interest.

This helps students build portfolios and gain hands-on experience.

---

### 📄 Resume Analyzer

Students can paste their resume and receive feedback on:

* Missing skills
* Resume improvements
* Project suggestions
* Internship readiness

---

### 🗺 Career Roadmap Generator

The AI generates a **personalized 6-month learning roadmap** based on:

* Student interests
* Current skills
* Available study time

This roadmap helps students plan their learning journey effectively.

---

### 📊 Skill Gap Analyzer

The AI analyzes the gap between:

* A student’s **current skills**
* Their **target career**

It then recommends:

* Missing skills
* Learning priorities
* Suggested projects

---

## Technologies Used

* Python
* Streamlit
* Groq API
* Llama-3.1 Large Language Model
* GitHub
* Streamlit Community Cloud (Deployment)

---

## System Architecture

```
User
  ↓
Streamlit Web Interface
  ↓
AI Mentor Logic
  ↓
Groq API
  ↓
Llama-3.1 Large Language Model
  ↓
Generated Career Guidance
```

---

## Installation

Clone the repository:

```
git clone https://github.com/your-username/ai-mentor-agent.git
cd ai-mentor-agent
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Environment Setup

Create an environment variable for the Groq API key:

Mac/Linux:

```
export GROQ_API_KEY="your_api_key"
```

Windows:

```
setx GROQ_API_KEY "your_api_key"
```

---

## Run the Application

Start the Streamlit app:

```
streamlit run app.py
```

The application will open in the browser.

---

## Deployment

The project is deployed using **Streamlit Community Cloud**.

Steps:

1. Push code to GitHub
2. Deploy using Streamlit Cloud
3. Add the `GROQ_API_KEY` in Streamlit Secrets

---

## Future Improvements

* Student profile system
* Career recommendation engine
* Internship opportunity suggestions
* Skill tracking dashboard
* Multi-agent mentoring system

---

## Conclusion

AI Mentor Agent demonstrates how **Large Language Models (LLMs)** can be used to build intelligent educational tools.
The system provides students with accessible career mentorship, personalized learning plans, and actionable guidance to support their professional growth.
