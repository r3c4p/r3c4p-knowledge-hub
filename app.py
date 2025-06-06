
import streamlit as st
import streamlit_authenticator as stauth

# Sample users (ganti dengan data nyata jika perlu)
names = ["Admin R3C4P"]
usernames = ["admin"]
passwords = stauth.Hasher(["r3c4p123"]).generate()

# Setup authenticator
authenticator = stauth.Authenticate(
    names,
    usernames,
    passwords,
    "r3c4p_cookie",
    "r3c4p_auth",
    cookie_expiry_days=1
)

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
