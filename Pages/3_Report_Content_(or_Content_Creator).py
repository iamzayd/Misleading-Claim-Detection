import streamlit as st
import mysql.connector as sql
from streamlit import session_state
import database as db
from deta import Deta
import os
import deta
from dotenv import load_dotenv
import pandas as pd

st.set_page_config(layout="wide")
# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)




# Function to insert reported content into the database
def insert_report():
    st.subheader("Insert Reported Content")
    C_Name = st.text_input("Enter Content Creator Name").strip()
    C_Link = st.text_input("Enter Link of the content :").strip()
    C_Des = st.text_area("Enter Report Description").strip()

    if st.button("Report Content"):
        a = db.insert_record(C_Name , C_Link , C_Des)
        
        st.success("Content Reported Successfully")


def get_C_Name(value):
    """Returns a record matching the provided C_Name."""
    records = db.fetch({"C_Name": value}).items
    return next(records, None)

def show_content_options():
    
    listTabs = ["All Reported Content", "By Content Creator"]
    tab1, tab2 = st.tabs(listTabs)
    
    with tab1:
        try:
            fetched_records = db.fetch_all_records()
            df = pd.DataFrame(fetched_records)
            df = df[["C_Name","C_Link","C_Des"]]

            # Streamlit UI
            st.title("Fetched Records Display")
            df.index = df.index + 1

            # Display the DataFrame as a table using st.table()
            st.table(df)
        except Exception as e:
            st.error("Database is empty!")

    with tab2:

        # Initialize session_state variables
        #if "C_Name2" not in session_state:
        #    session_state.C_Name2 = ""

        C_Name = st.text_input("Enter Content Creator Name:")
        if C_Name:
            try:
                fetched_record = db.get_C_Name(C_Name)
                df = pd.DataFrame(fetched_record)
                df = df[["C_Name","C_Link","C_Des"]]
                df.index = df.index + 1
                st.table(df)

            except Exception as e:
                st.error("Record Doesnt Exist in the Database.")

def check_credentials(username, password, cursor):
    query = "SELECT COUNT(*) FROM user_credentials WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()[0]
    return result


    # Function to view reported content from the database
def view_report():
    my_db = sql.connect(host='localhost', user='root', password='root', database='Report')
    cursor = my_db.cursor()

    st.subheader("View Reported Content")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if password:
        if check_credentials(username, password, cursor):
                st.success("Login successful!")
                show_content_options()
        else:
            st.error("Invalid credentials")
    






# Main Streamlit app
def main():
    my_db = sql.connect(host='localhost', user='root', password='root', database='Report')
    cursor = my_db.cursor()

    task = st.sidebar.selectbox("Choose a task", ["Report Data", "View Reported Data"],key = "task")

    if task == "Report Data":
        insert_report()
    elif task == "View Reported Data":
        view_report()

if __name__ == "__main__":
    main()

st.sidebar.write("-----------------")
st.sidebar.markdown('''
Created with 💜 by [Najeeb](https://www.instagram.com/thiscloudbook/) And [Karthik](https://www.instagram.com/_mr_thop/).
''')
