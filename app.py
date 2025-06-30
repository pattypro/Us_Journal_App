
import streamlit as st
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

# Google authentication (must be done via OAuth in local mode)
def authenticate_google_drive():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    return GoogleDrive(gauth)

# Streamlit UI
st.title("📝 US Journal App with Google Drive Upload")
st.markdown("Write and save your journal entries to Google Drive.")

journal_text = st.text_area("Write your thoughts here:", height=200)
file_name = st.text_input("Enter a file name (e.g., 'my_journal.txt')")

if st.button("Upload to Google Drive"):
    if journal_text and file_name:
        try:
            drive = authenticate_google_drive()
            file = drive.CreateFile({'title': file_name})
            file.SetContentString(journal_text)
            file.Upload()
            st.success(f"File '{file_name}' successfully uploaded to your Google Drive.")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter both journal text and a file name.")
