# 📘 Smart Study Plan Generator

## 🔹 Overview
The *Smart Study Plan Generator* is an *AI-powered system* that helps students create *personalized study plans* based on their *academic profile, learning style, and available time*.  
Using *deep learning models, it predicts optimal study hours per subject and automatically maps them into a **structured weekly timetable, displayed through an **interactive Streamlit interface*.

This project helps learners:

- 📅 Organize their study schedules effectively  
- ⏰ Manage time efficiently based on available slots  
- 🧠 Receive adaptive, AI-driven study hour recommendations  
- 📊 Visualize their personalized timetables interactively  

---

## 🔹 Completed Work (Work Done ✅)

### *Phase 1 – Problem Definition*
- Defined the main goal: build an AI-driven system to generate personalized study plans.  
- Identified input parameters: *GPA, **learning style, **available hours, **subject count, **exam priority, and **weak subjects*.  
- Defined outputs: *recommended study hours per subject* and *auto-generated timetable*.

### *Phase 2 – Dataset Creation*
- Created a *synthetic dataset* of *2000 student profiles* with realistic academic and behavioral patterns.  
- Dataset includes:
  - student_id
  - gpa
  - learning_style (Visual / Auditory / Kinesthetic)
  - available_hours_per_day
  - free_days_per_week
  - subject_count
  - exam_priority
  - weak_subjects_count
  - recommended_hours_per_subject (calculated based on patterns)

### *Phase 3 – Model Development*
- Built a *Deep Neural Network (DNN)* using *TensorFlow/Keras* to predict study hours per subject.  
- Preprocessing:
  - *Standard scaling* for numeric features  
  - *One-hot encoding* for categorical features  
- Implemented training optimizations:
  - *Early stopping, **learning rate reduction, and **checkpointing*  
- Model saved and validated for real-time predictions.

### *Phase 3.5 – Scheduler Logic*
- Developed a *weekly timetable generator* that:
  - Distributes predicted study hours across available days.  
  - Allocates additional time to weak subjects.  
  - Generates both *detailed* and *summary* versions of the schedule.  
  - Exports data to *CSV* for reuse or analysis.

### *Phase 4 – Streamlit Integration ✅ (Completed)*
- Successfully integrated the AI model and scheduler into a *Streamlit web app*.  
- Added an *interactive interface* where users can:
  - Input their academic and personal details.  
  - View predicted study hours and personalized timetables.  
  - Download their generated schedules.  
- Included *visual charts* (Matplotlib/Plotly) for easy analysis.  

---

## 🔹 Upcoming Work (Next Steps 🚀)

### *Phase 5 – Testing & Visualization Enhancement*
- Conduct large-scale testing with multiple user profiles.  
- Refine UI with improved visuals, charts, and responsive layout.  

### *Phase 6 – Documentation & Deployment*
- Finalize *project documentation*, user guide, and code comments.  
- Deploy the final Streamlit app on *Streamlit Cloud*.  
- Push source code and documentation to *GitHub*.

### *Phase 7 – Final Presentation & Demo*
- Prepare slides, demo video, and report for project presentation.

---

## 🔹 Tech Stack

| Category | Tools / Libraries |
|-----------|------------------|
| *Language* | Python 🐍 |
| *Libraries* | NumPy, Pandas, TensorFlow/Keras, Streamlit, Matplotlib, Plotly |
| *Development Tools* | Jupyter Notebook / Google Colab |
| *Version Control* | Git & GitHub |
| *Deployment* | Streamlit Cloud |

---

## 🔹 Project Status
✅ *Phases 1–4 Completed* (Problem Definition, Dataset Creation, Model Training, Scheduler Logic, Streamlit Integration)  
🚧 *Currently Working On:* Phase 5 – Testing & Visualization Enhancement  
🎯 *Next Goal:* Refine visualizations and prepare for deployment.

---

## 🔹 Output Got

![WhatsApp Image 2025-10-31 at 08 51 30_2f5c16e7](https://github.com/user-attachments/assets/ce792558-bab8-4396-871d-5826f31a9204)

![WhatsApp Image 2025-10-31 at 08 51 49_78164be5](https://github.com/user-attachments/assets/ed527927-35e0-4c04-8075-d48648bc5a2a)

![WhatsApp Image 2025-10-31 at 08 52 34_bb970b4c](https://github.com/user-attachments/assets/465180b9-ec4e-498d-8dbf-876b3f91282e)


