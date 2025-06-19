
import streamlit as st
from datetime import date

st.set_page_config(page_title="Us Journal", page_icon="💑", layout="centered")

st.title("💖 Our Private Journal")
st.subheader("A space to grow together, one entry at a time.")

# Create input form
with st.form("entry_form"):
    st.write("### ✍️ New Journal Entry")

    entry_date = st.date_input("Date", value=date.today())
    mood = st.selectbox("Mood", ["😊 Happy", "😢 Sad", "🤔 Thoughtful", "❤️ In Love", "🙏 Grateful"])
    message = st.text_area("Write something for us...", height=200)

    submitted = st.form_submit_button("Save Entry 💌")
    if submitted:
        with open("journal.txt", "a", encoding="utf-8") as file:
            file.write(f"{entry_date} | {mood} | {message}\n\n")
        st.success("Entry saved! ❤️")
