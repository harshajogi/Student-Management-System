import streamlit as st
import sqlite3
import pandas as pd

# Database connection
conn = sqlite3.connect("students.db")

cursor = conn.cursor()
st.set_page_config(
    page_title="Student Management System",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
    <style>

    .stApp {
        background-color: #0f172a;
        color: white;
    }

    [data-testid="stSidebar"] {
        background-color: #1e293b;
    }

    h1 {
        color: #38bdf8;
        text-align: center;
    }

    .stButton>button {
        background-color: #38bdf8;
        color: black;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 16px;
    }

    .stButton>button:hover {
        background-color: #0ea5e9;
        color: white;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# App title
st.title("🎓 Student Management System")
st.write("------------------------------")
st.sidebar.title("Navigation")

menu = "Home"

if st.sidebar.button("Home"):
    menu = "Home"

if st.sidebar.button("Add Student"):
    menu = "Add Student"

if st.sidebar.button("View All Students"):
    menu = "View All Students"

if st.sidebar.button("Delete Student"):
    menu = "Delete Student"

if st.sidebar.button("Update Student"):
    menu = "Update Student"

if menu=="Home":
    st.header("Welcome to SMS")
    st.header("Manage your student Details")
# Add student
if menu == "Add Student":
    name = st.text_input("Enter Student Name")

    age = st.number_input(
    "Enter Age",
    min_value=1,
    max_value=100
    )

    branch = st.selectbox(
    "Select Branch",
    ["CSE", "ECE", "EEE", "MECH", "CIVIL"]
    )

    marks = st.number_input(
    "Enter Marks",
    min_value=0,
    max_value=100
    )
    if marks < 0 or marks > 100:
        st.error("Invalid Marks")
    if st.button("Add Student"):
        if name == "":
            st.error("Name cannot be empty")
        else:
            cursor.execute(
                """
                INSERT INTO students(name, age, branch, marks)
                VALUES (?, ?, ?, ?)
                """,
                (name, age, branch, marks)
             )

            conn.commit()

            st.success("Student Added Successfully!")


# View students
if menu == "View All Students":

    
    cursor.execute("SELECT * FROM students")

    data = cursor.fetchall()

    

    df = pd.DataFrame(
        data,
        columns=["ID", "Name", "Age", "Branch", "Marks"]
    )

    st.dataframe(df)

    st.success("Student viewed successfully!")


if menu == "Delete Student":
    st.write("## Delete Student")

    delete_id = st.number_input(
        "Enter Student ID to Delete",
        min_value=1,
        step=1
    )

    if st.button("Delete Student"):

        cursor.execute(
            "DELETE FROM students WHERE id = ?",
            (delete_id,)
        )

        conn.commit()

        st.success("Student Deleted Successfully!")
if menu =="Update Student":    
    st.write("## Update Student")

    update_id = st.number_input(
        "Enter Student ID to Update",
        min_value=1,
        step=1,
        key="update_id"
    )

    new_name = st.text_input(
        "Enter New Name",
        key="new_name"
    )

    new_age = st.number_input(
        "Enter New Age",
        min_value=1,
        max_value=100,
        key="new_age"
    )

    new_branch = st.selectbox(
        "Select New Branch",
        ["CSE", "ECE", "EEE", "MECH", "CIVIL"],
        key="new_branch"
    )

    new_marks = st.number_input(
        "Enter New Marks",
        min_value=0,
        max_value=100,
        key="new_marks"
    )

    if st.button("Update Student"):

        cursor.execute(
            """
            UPDATE students
            SET name = ?, age = ?, branch = ?, marks = ?
            WHERE id = ?
            """,
            (
                new_name,
                new_age,
                new_branch,
                new_marks,
                update_id
            )
        )

        conn.commit()

        st.success("Student Updated Successfully!")

