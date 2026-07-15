import pandas as pd
df = pd.read_csv("W:/ML LEARNINGS/ML-Engineer-Journey/Machine-Learning/Day 2/assisment 1/student.csv")
print(df)
print("the average marks:",df["Marks"].mean())
topper = df.loc[df["Marks"].idxmax()]
print("the topper name and its mark:", topper["Name"], topper["Marks"])
print("the students above 80:\n", df[df["Marks"] > 80][["Name", "Marks","Age"]].to_csv(index=False))
print("the student details has been updated")
