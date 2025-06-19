import streamlit as st
from datetime import date
import os

# ---------- CONFIG ----------
st.set_page_config(page_title="Us Journal 💑", page_icon="💖", layout="centered")

# ---------- SIMPLE PASSWORD LOGIN ----------
def check_login():
    password = st.text_input("Enter Secret Code to Access the Journal 🔐", type="password")
    if password == "oursecret123":
        st.success("Welcome to Our Journal! 💌")
        return True
    elif password:
        st.error("Incorrect password. Try again.")
    return False

if not check_login():
    st.stop()

# ---------- JOURNAL ENTRY ----------
st.title("💖 Our Private Journal")
st.subheader("A space to grow together, one entry at a time.")

with st.form("entry_form"):
    st.write("### ✍️ Add New Entry")
    entry_date = st.date_input("Date", value=date.today())
    mood = st.selectbox("Mood", ["😊 Happy", "😢 Sad", "🤔 Thoughtful", "❤️ In Love", "🙏 Grateful"])
    message = st.text_area("Write something for us...", height=200)
    submitted = st.form_submit_button("Save Entry 💌")

    if submitted:
        with open("journal.txt", "a", encoding="utf-8") as file:
            file.write(f"{entry_date} | {mood} | {message}\n")
        st.success("Entry saved! 💖")

# ---------- JOURNAL VIEWER ----------
st.write("### 📖 View Past Entries")

if os.path.exists("journal.txt"):
    with open("journal.txt", "r", encoding="utf-8") as file:
        entries = file.readlines()
        for entry in reversed(entries):
            parts = entry.strip().split(" | ")
            if len(parts) == 3:
                edate, emood, emessage = parts
                with st.expander(f"{edate} {emood}"):
                    st.write(emessage)
else:
    st.info("No entries yet. Start journaling your love story! 🥰")