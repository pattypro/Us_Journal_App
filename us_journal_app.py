import streamlit as st
from datetime import date
import os
from PIL import Image

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
    image = st.file_uploader("Optional: Upload a photo to remember this moment 📸", type=["jpg", "jpeg", "png"])
    submitted = st.form_submit_button("Save Entry 💌")

    if submitted:
        entry_filename = f"{entry_date}_{mood.replace(' ', '_')}.txt"
        with open(f"entries/{entry_filename}", "w", encoding="utf-8") as file:
            file.write(f"{entry_date} | {mood} | {message}\n")

        if image:
            image_path = f"entries/{entry_date}_{mood.replace(' ', '_')}.jpg"
            with open(image_path, "wb") as img_file:
                img_file.write(image.read())

        st.success("Entry saved! 💖")

# ---------- JOURNAL VIEWER ----------
st.write("### 📖 View Past Entries")

if os.path.exists("entries"):
    entry_files = sorted([f for f in os.listdir("entries") if f.endswith(".txt")], reverse=True)
    for file_name in entry_files:
        with open(f"entries/{file_name}", "r", encoding="utf-8") as file:
            content = file.readline().strip()
            if content:
                edate, emood, emessage = content.split(" | ")
                with st.expander(f"{edate} {emood}"):
                    st.write(emessage)
                    image_name = file_name.replace(".txt", ".jpg")
                    image_path = f"entries/{image_name}"
                    if os.path.exists(image_path):
                        st.image(image_path, caption="Memory Photo", use_column_width=True)
else:
    st.info("No entries yet. Start journaling your love story! 🥰")