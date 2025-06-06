import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# Load YAML config
with open("config_r3c4p_auth.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

# Setup authenticator
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

# Login UI
name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status:
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Selamat datang, {name}")
    st.title("🔐 R3C4P Knowledge Hub")
    st.write("Anda berhasil login dan dapat mengakses fitur analisa pelanggan.")
elif authentication_status is False:
    st.error("Username atau password salah.")
elif authentication_status is None:
    st.warning("Silakan masukkan username dan password.")
