import streamlit as st
import json
import os
from datetime import datetime

st.set_page_config(page_title="Smart Study Plan Generator", layout="wide")

st.title("🎯 Smart Study Plan Generator")
st.subheader("Track your daily learning progress and stay consistent!")

if "today_tasks" not in st.session_state:
    st.session_state["today_tasks"] = [
        "Revise Linear Regression concepts",
        "Practice SQL Joins problems",
        "Watch 30-min AI tutorial video",
        "Complete Python project tasks",
        "Read an article on Deep Learning"
    ]

progress_file = "progress.json"

if os.path.exists(progress_file):
    with open(progress_file, "r") as f:
        progress_data = json.load(f)
else:
    progress_data = {}

today = datetime.now().strftime("%Y-%m-%d")
completed_tasks = progress_data.get(today, [])

st.header("📚 Today's Study Tasks")

checked = []
for i, task in enumerate(st.session_state["today_tasks"]):
    done = st.checkbox(task, value=(task in completed_tasks), key=f"task_{i}")
    if done:
        checked.append(task)

progress_data[today] = checked
with open(progress_file, "w") as f:
    json.dump(progress_data, f)

total_tasks = len(st.session_state["today_tasks"])
completed = len(checked)
progress = completed / total_tasks if total_tasks else 0
st.progress(progress)
st.write(f"✅ {completed}/{total_tasks} tasks completed today")

if st.button("📊 Show My Past Progress"):
    if progress_data:
        st.subheader("Your Past Study Progress")
        for day, tasks in progress_data.items():
            st.write(f"**{day}:** {len(tasks)} tasks completed ✅")
    else:
        st.info("No progress data found yet. Complete today's tasks to get started!")

st.caption("💡 Tip: Come back daily to check your progress and build consistency.")
