
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
authenticator.login()

if st.session_state["authentication_status"]:
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Selamat datang, {st.session_state['name']}")
    st.title("🔐 R3C4P Knowledge Hub")
    st.write("Anda berhasil login dan dapat mengakses fitur analisa pelanggan.")
elif st.session_state["authentication_status"] is False:
    st.error("Username atau password salah.")
elif st.session_state["authentication_status"] is None:
    st.warning("Silakan masukkan username dan password.")
