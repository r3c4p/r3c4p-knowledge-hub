
import streamlit as st
from urllib.parse import urlencode

# Constants - REPLACE with your actual values
CLIENT_ID = "YOUR_GOOGLE_CLIENT_ID"
REDIRECT_URI = "https://YOUR-STREAMLIT-APP.streamlit.app"
SCOPE = "openid email profile"
AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"

def get_login_url():
    params = {
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
        "scope": SCOPE,
        "access_type": "offline",
        "prompt": "consent"
    }
    return f"{AUTH_URL}?{urlencode(params)}"

# Streamlit App
st.set_page_config(page_title="R3C4P OAuth Login", layout="centered")

st.title("🔐 Login dengan Akun Google")
st.write("Klik tombol di bawah untuk login menggunakan akun Gmail Anda.")

login_url = get_login_url()
st.markdown(f"[Login dengan Google]({login_url})", unsafe_allow_html=True)

st.info("Setelah login, Anda akan diarahkan kembali ke aplikasi Streamlit.")
