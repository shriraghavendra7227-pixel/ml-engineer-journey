import pandas as pd

df = pd.read_csv(r"W:\ML LEARNINGS\ML-Engineer-Journey\Machine-Learning\Day 2\assisment 1\student.csv")

while True:
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    marks = int(input("Enter marks: "))

    df.loc[len(df)] = [name, age, marks]

    choice = input("Add another student? (yes/no): ").lower()

    if choice != "yes":
        break

df.to_csv(r"W:\ML LEARNINGS\ML-Engineer-Journey\Machine-Learning\Day 2\assisment 1\student.csv", index=False)

print("\nFinal Student Data:")
print(df)