import streamlit as st
import mysql.connector as sql
from streamlit import session_state



# Function to insert reported content into the database
def insert_report(cursor, my_db):
    st.subheader("Insert Reported Content")
    C_ID = st.number_input("Enter Content ID", step=1)
    C_Name = st.text_input("Enter Content Creator Name").strip()
    C_Link = st.text_input("Enter Link of the content :").strip()
    C_Des = st.text_area("Enter Report Description").strip()

    if st.button("Report Content"):
        values = (C_ID, C_Name , C_Link , C_Des)
        query = 'INSERT INTO Data (C_ID, C_Name, C_Link, C_Des) VALUES (%s, %s, %s, %s)'
        cursor.execute(query, values)
        my_db.commit()
        st.success("Content Reported Successfully")



def check_credentials(username, password, cursor):
    query = "SELECT COUNT(*) FROM user_credentials WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()[0]
    return result


def show_content_options(cursor):
    
    listTabs = ["All Reported Content", "By Content Creator"]
    tab1, tab2 = st.tabs(listTabs)
    
    with tab1:

        query = 'SELECT C_ID, C_Name, C_Link, C_Des FROM Data'
        cursor.execute(query)
        data = cursor.fetchall()
        if data:
            st.write("Reported Content:")
            st.write("---")
            for row in data:
                st.write("Content ID:", row[0])
                st.write("Creator Name:", row[1])
                st.write("Content Link:", row[2])
                st.write("Report Description:", row[3])
                st.write("---")
        else:
            st.warning("No reported content found.")

# ... Assuming you have your database connection and cursor defined ...

    with tab2:

        # Initialize session_state variables
        #if "C_Name2" not in session_state:
        #    session_state.C_Name2 = ""

        C_Name2 = st.text_input("Enter Content Creator Name 2")
        st.write(C_Name2)

        if C_Name2:
            query = 'SELECT C_ID, C_Name, C_Link, C_Des FROM Data WHERE C_Name = %s'
            cursor.execute(query, (C_Name2,))
            data = cursor.fetchall()

            if data:
                st.write(f"Reported Content by '{C_Name2}':")
                for row in data:
                    st.write("Content ID:", row[0])
                    st.write("Creator Name:", row[1])
                    st.write("Content Link:", row[2])
                    st.write("Report Description:", row[3])
                    st.write("---")
            else:
                st.write(f"No reported content found for '{C_Name2}'.")


    # Function to view reported content from the database
def view_report(cursor):
    st.subheader("View Reported Content")




    username = st.text_input("Username")
    password = st.text_input("Password", type="password")


    # Button to check credentials
    if st.button("Login"):
        
        if check_credentials(username, password, cursor):
            st.success("Login successful!")
            show_content_options(cursor)
        else:
            st.error("Invalid credentials")






# Main Streamlit app
def main():

    
    #st.title("Data Reporting Interface")
    #st.write("Welcome to the Data Reporting Interface")

    # Establish database connection
    my_db = sql.connect(host='localhost', user='root', password='root', database='Report')
    cursor = my_db.cursor()



    task = st.sidebar.selectbox("Choose a task", ["Report Data", "View Reported Data"],key = "task")

    if task == "Report Data":
        insert_report(cursor, my_db)
    elif task == "View Reported Data":
        view_report(cursor)

    # Close database connection
    my_db.close()

if __name__ == "__main__":
    main()
