

import streamlit as st
import sqlite3
from streamlit_option_menu import option_menu

def connect_db():
    conn = sqlite3.connect("mydatabase.db")
    return conn

def create_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student (name text, password text, roll int, branch text)")
    conn.commit()
    conn.close()

def add_record(data):
    conn = connect_db()
    cur = conn.cursor()
    try:
        cur.execute('INSERT INTO student(name, password, roll, branch) VALUES(?, ?, ?, ?)', data)
        conn.commit()
        st.success("Student Registered")
    except sqlite3.IntegrityError:
        st.error("User  already exists")
    except Exception as e:
        st.error(f"An error occurred: {e}")
    finally:
        conn.close()

def view_record():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")
    result = cur.fetchall()
    conn.close()
    return result

def display():
    data = view_record()
    # st.write(data)
    st.table(data)

def signup():
    st.title("Registration Page")
    name = st.text_input("Enter your Name")
    rollno = st.text_input("Enter Your Roll No")
    branch = st.selectbox('Choose Branch', ['CSE', 'AIML', 'IOT', 'IT'])
    password = st.text_input("Enter a password", type="password")
    repass = st.text_input("Confirm password", type="password")
    
    if st.button("Sign Up"):
        if password != repass:
            st.error("Passwords do not match")
        else:
            try:
                rollno = int(rollno)  # Convert roll number to integer
                add_record((name, password, rollno, branch))
            except ValueError:
                st.error("Roll number must be an integer")

create_table()

with st.sidebar:
    selected = option_menu("Select from HERE", ["Sign up", "Display Record"])

if selected == "Sign up":
    signup()
else:
    display()

