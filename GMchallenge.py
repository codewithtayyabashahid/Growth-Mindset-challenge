import streamlit as st
import pandas as pd
import random

# Streamlit Page Configurations
st.set_page_config(page_title="Student Data Generator", layout="wide")
st.title("Student CSV File Generator")

# Define possible values
names = ["Fatima", "Ali", "Laiba", "Abiha", "Saad", "Hassan", "Hamza", "Abdullah",
         "Shahwaiz", "Tayyaba", "Fiza", "Ezza"]
grades = ["A", "B", "C", "D", "E", "F"]

# Generate multiple students (Example: 10 students)
students = []
for i in range(1, 11):  # Generate 10 student records
    student = {
        "ID": i,
        "Name": random.choice(names),  # Convert set to list
        "Age": random.randint(18, 25),
        "Grade": random.choice(grades),
        "Marks": random.randint(40, 100),
    }
    students.append(student)

# Convert the list of students to a DataFrame
df = pd.DataFrame(students)

# Display the data
st.subheader("Generated Students Data")
st.dataframe(df)

# Convert DataFrame to CSV
csv_file = df.to_csv(index=False).encode('utf-8')

# Download button
st.download_button("Download CSV File", csv_file, "students.csv", "text/csv")

# Success Message
st.success("Students Record Generated Successfully!!!")
