import pandas as pd
import numpy as np
import random

# Number of synthetic records
n = 1000

# Possible categories
learning_styles = ["Visual", "Reading", "Kinesthetic", "Auditory"]
exam_priorities = ["Low", "Medium", "High"]

# Empty dataset list
data = []

for i in range(1, n+1):
    gpa = round(np.random.uniform(5.0, 10.0), 2)  # GPA between 5.0 and 10.0
    learning_style = random.choice(learning_styles)
    available_hours = random.randint(2, 8)  # daily free hours
    free_days = random.randint(3, 7)  # free study days per week
    subject_count = random.randint(4, 8)  # number of subjects
    exam_priority = random.choice(exam_priorities)
    weak_subjects = random.randint(0, 3)
    
    # Simple formula for recommended study hours (can be improved later with ML)
    base_hours = available_hours * (free_days / 7) / subject_count
    priority_factor = {"Low": 0.8, "Medium": 1.0, "High": 1.2}[exam_priority]
    weak_factor = 1 + (0.1 * weak_subjects)
    
    recommended_hours = round(base_hours * priority_factor * weak_factor, 2)
    
    data.append([i, gpa, learning_style, available_hours, free_days, subject_count, 
                 exam_priority, weak_subjects, recommended_hours])

# Create DataFrame
columns = ["Student_ID", "GPA", "Learning_Style", "Available_Hours_Per_Day", 
           "Free_Days_Per_Week", "Subject_Count", "Exam_Priority", 
           "Weak_Subjects_Count", "Recommended_Hours_Per_Subject"]

df = pd.DataFrame(data, columns=columns)

# Save dataset
df.to_csv("study_plan_dataset.csv", index=False)

print("✅ Synthetic dataset generated and saved as 'study_plan_dataset.csv'")
print(df.head())
