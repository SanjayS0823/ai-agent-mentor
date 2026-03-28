import streamlit as st
from mentor_logic import (
    career_guidance,
    recommend_courses,
    generate_projects,
    analyze_resume,
    generate_roadmap,
    skill_gap_analysis
)

# ---------------------------
# Page Configuration
# ---------------------------

st.set_page_config(
    page_title="AI Mentor Agent",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI Mentor Agent")

st.markdown(
    "An AI-powered mentor that helps students with **career guidance, project ideas, courses, and resume feedback**."
)

# ---------------------------
# Sidebar
# ---------------------------

st.sidebar.title("🎓 AI Mentor")
st.sidebar.markdown("### Navigation")

page = st.sidebar.radio(
    "",
    [
        "💬 Career Chat Mentor",
        "📚 Course Recommendations",
        "💡 Project Ideas",
        "📄 Resume Analyzer",
        "🗺 Career Roadmap",
        "📊 Skill Gap Analyzer"
    ]
)

st.sidebar.markdown("---")

if st.sidebar.button("🗑 Clear Chat"):
    if "messages" in st.session_state:
        st.session_state.messages = []

# ---------------------------
# Career Chat Mentor
# ---------------------------

if page == "💬 Career Chat Mentor":

    st.header("💬 AI Career Mentor")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    user_input = st.chat_input("Ask about careers, skills, or learning paths...")

    if user_input:

        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        with st.chat_message("user"):
            st.write(user_input)

        with st.spinner("Thinking..."):

            reply = career_guidance(st.session_state.messages, user_input)

        st.session_state.messages.append(
            {"role": "assistant", "content": reply}
        )

        with st.chat_message("assistant"):
            st.write(reply)

# ---------------------------
# Course Recommendations
# ---------------------------

elif page == "📚 Course Recommendations":

    st.header("📚 Recommended Courses")

    field = st.selectbox(
        "Select Career Field",
        [
            "Artificial Intelligence",
            "Data Science",
            "Web Development",
            "Cybersecurity",
            "Cloud Computing"
        ]
    )

    if st.button("Get Courses"):

        with st.spinner("Finding courses..."):
            courses = recommend_courses(field)

        st.write(courses)

# ---------------------------
# Project Ideas
# ---------------------------

elif page == "💡 Project Ideas":

    st.header("💡 Project Idea Generator")

    field = st.selectbox(
        "Select Field",
        [
            "Artificial Intelligence",
            "Data Science",
            "Web Development"
        ]
    )

    if st.button("Generate Projects"):

        with st.spinner("Generating ideas..."):
            projects = generate_projects(field)

        st.write(projects)

# ---------------------------
# Resume Analyzer
# ---------------------------

elif page == "📄 Resume Analyzer":

    st.header("📄 Resume Feedback")

    resume = st.text_area(
        "Paste your resume text here",
        height=200
    )

    if st.button("Analyze Resume"):

        if resume.strip() == "":
            st.warning("Please paste your resume.")
        else:

            with st.spinner("Analyzing resume..."):
                feedback = analyze_resume(resume)

            st.write(feedback)

# ---------------------------
# Career Roadmap
# ---------------------------

elif page == "🗺 Career Roadmap":

    st.header("🗺 Personalized Career Roadmap")

    name = st.text_input("Your Name")
    degree = st.text_input("Your Degree / Major")

    interests = st.text_input(
        "Career Interests (e.g., AI, Data Science, Web Development)"
    )

    skills = st.text_input("Current Skills")

    hours = st.selectbox(
        "How many hours can you study per week?",
        ["5 hours", "10 hours", "15 hours", "20+ hours"]
    )

    if st.button("Generate Roadmap"):

        profile = f"""
        Name: {name}
        Degree: {degree}
        Interests: {interests}
        Current Skills: {skills}
        Weekly Study Time: {hours}
        """

        with st.spinner("Creating your personalized roadmap..."):
            roadmap = generate_roadmap(profile)

        st.subheader("Your 6-Month Career Roadmap")
        st.write(roadmap)

# ---------------------------
# Skill Gap Analyzer
# ---------------------------

elif page == "📊 Skill Gap Analyzer":

    st.header("📊 Skill Gap Analyzer")

    goal = st.text_input(
        "Target Career",
        placeholder="Example: Machine Learning Engineer"
    )

    skills = st.text_area(
        "Your Current Skills",
        placeholder="Example: Python basics, data analysis"
    )

    if st.button("Analyze Skills"):

        with st.spinner("Analyzing skill gap..."):
            result = skill_gap_analysis(goal, skills)

        st.subheader("Skill Gap Report")
        st.write(result)

# ---------------------------
# Footer
# ---------------------------

st.markdown("---")
st.caption("AI Mentor Agent • Built with Python, Streamlit, and Llama 3")