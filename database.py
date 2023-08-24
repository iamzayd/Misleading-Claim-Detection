import streamlit as st  # pip install streamlit
from deta import Deta  # pip install deta
import os

from deta import Deta

from dotenv import load_dotenv
load_dotenv(r"C:\Users\Najeeb\Desktop\SIT Semesters\Sem 5\Hackathon investors\.env.txt")

# Load the environment variables
DETA_KEY = os.getenv("DETA_KEY")



# Initialize with a project key
deta = Deta(DETA_KEY)

# This is how to create/connect a database
db = deta.Base("Report")



def insert_record(C_Name, C_Link, C_Des):
    """Returns the report on a successful creation, otherwise raises an error"""
    return db.put({"C_Name": C_Name, "C_Link": C_Link, "C_Des": C_Des})


def fetch_all_records():
    """Returns a dict of all periods"""
    res = db.fetch()
    return res.items


def get_C_Name(value):
    records = db.fetch({"C_Name": value}).items
    return records