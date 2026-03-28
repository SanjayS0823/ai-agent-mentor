# AI Mentor Agent 🎓

## Overview

AI Mentor Agent is a web-based application designed to guide students in choosing and preparing for their careers.
The system acts like a virtual mentor that answers career-related questions and suggests skills, learning paths, and project ideas.

Students can ask questions about different career paths such as Data Science, Artificial Intelligence, Web Development, and more.
The AI mentor provides structured guidance to help students plan their learning journey.

---

## Problem Statement

Many students struggle to decide which career path to follow and what skills they should learn.
They often lack proper mentorship and guidance.
This project aims to provide an AI-powered mentor that helps students understand career options and build a clear roadmap for their future.

---

## Features

* Career guidance for students
* Skill recommendations for different careers
* Learning roadmaps for various technology fields
* Suggestions for projects and internships
* Interactive question-answer interface
* Simple web-based user interface

---

## Technologies Used

* Python
* Streamlit
* Transformers (LLM Model)
* PyTorch
* GitHub

---

## Project Structure

```
ai-mentor-agent
│
├── app.py
├── mentor_logic.py
├── requirements.txt
└── README.md
```

---

## How It Works

1. The student enters a career-related question in the web interface.
2. The AI Mentor Agent processes the question.
3. A language model generates a response.
4. The system provides career advice including skills, learning roadmap, and project suggestions.

---

## Installation

Clone the repository:

```
git clone https://github.com/yourusername/ai-mentor-agent.git
```

Navigate to the project folder:

```
cd ai-mentor-agent
```

Install required dependencies:

```
pip install -r requirements.txt
```

---

## Running the Application

Run the Streamlit application using:

```
streamlit run app.py
```

The application will open in the browser at:

```
http://localhost:8501
```

---

## Example Questions

Students can ask questions such as:

* How do I become a Machine Learning Engineer?
* What skills are required for Data Science?
* What should a CSE student learn in the second year?
* How can I start a career in Web Development?

---

## Future Improvements

* Personalized career recommendations
* Student profile analysis
* Resume feedback system
* Internship and course recommendations
* Multi-agent mentoring system

---

## Conclusion

AI Mentor Agent demonstrates how artificial intelligence can support students in making informed career decisions.
By providing accessible and interactive mentorship, the system helps students explore career opportunities and plan their learning journey effectively.
