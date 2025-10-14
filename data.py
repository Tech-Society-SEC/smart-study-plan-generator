import pandas as pd
import numpy as np

num_rows = 2000

data = {
    "Student_ID": range(1, num_rows + 1),
    "GPA": np.round(np.random.uniform(5.0, 10.0, num_rows), 2),
    "Learning_Style": np.random.choice(["Visual", "Auditory", "Kinesthetic"], num_rows),
    "Available_Hours_Per_Day": np.random.randint(2, 8, num_rows),
    "Free_Days_Per_Week": np.random.randint(0, 2, num_rows),
    "Subject_Count": np.random.randint(4, 8, num_rows),
    "Exam_Priority": np.random.choice(["High", "Medium", "Low"], num_rows),
    "Weak_Subjects_Count": np.random.randint(0, 4, num_rows)
}

df_synthetic = pd.DataFrame(data)

df_synthetic["Recommended_Hours_Per_Subject"] = (
    5 - df_synthetic["GPA"] / 2 + df_synthetic["Weak_Subjects_Count"] * 0.5
).round(2)

df_synthetic.to_csv("study_plan_dataset_2000.csv", index=False)
