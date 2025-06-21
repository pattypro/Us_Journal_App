# 💖 Us Journal with Google Drive Upload (Fixed Version)

A private, secure, and romantic journal app for couples — built using Streamlit, with cloud backup via Google Drive.

## 🌟 Features
- Write daily/weekly journal entries
- Upload a memory photo for each entry
- View saved entries with date, mood, and message
- Password login to protect your love story
- Automatically uploads data to Google Drive

## 🛠️ Requirements
- Python 3.x
- `streamlit`, `pydrive`, `pillow`

## 🔐 Setup Google Drive API
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a project and enable **Google Drive API**
3. Create **OAuth credentials** (Desktop app)
4. Download `client_secrets.json` and place it in the same folder as the app

## ▶️ How to Run
```bash
pip install streamlit pydrive pillow
streamlit run us_journal_app.py
```

Default password: `oursecret123`