
import streamlit as st
import requests
from datetime import datetime

st.title("📝 US Journal App - File.io Upload (No Google API)")
st.markdown("Write your journal entry and upload it securely to File.io. No login or API required.")

journal_text = st.text_area("Write your thoughts here:", height=200)
file_name = st.text_input("Enter a file name (e.g., 'my_journal.txt')", f"journal_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")

if st.button("Upload to File.io"):
    if journal_text and file_name:
        try:
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(journal_text)
            with open(file_name, "rb") as file:
                response = requests.post("https://file.io", files={"file": file})
            if response.status_code == 200:
                url = response.json()["link"]
                st.success(f"✅ Uploaded! [Click to Download]({url})")
            else:
                st.error("Upload failed. Please try again.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please write something and name your file.")
