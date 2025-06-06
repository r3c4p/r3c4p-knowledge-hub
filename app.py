import streamlit as st
import streamlit_authenticator as stauth
import openai
import yaml
import pandas as pd
from yaml.loader import SafeLoader

# Load OpenAI API key
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

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

# Login
name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status:
    authenticator.logout("Logout", "sidebar")

    st.sidebar.markdown("### R3C4P Knowledge Hub")
    st.sidebar.markdown("Welcome, how can I assist you today?")

    if 'page' not in st.session_state:
        st.session_state.page = "Identify a customer"

    if st.sidebar.button("Identify a customer"):
        st.session_state.page = "Identify a customer"
    if st.sidebar.button("Map pain points"):
        st.session_state.page = "Map pain points"
    if st.sidebar.button("Construct business model"):
        st.session_state.page = "Construct business model"
    if st.sidebar.button("Retrieve insights"):
        st.session_state.page = "Retrieve insights"

    # Main Content
    st.title(st.session_state.page)

    if st.session_state.page == "Identify a customer":
        st.write("Generate company profile and analysis based on R3C4P framework.")
        customer_name = st.text_input("Customer name", "PT Industri Jaya Komponen")
        level = st.selectbox("Analysis level", ["Corporate Group", "Corporate", "Division", "Project", "Subsidiary"])

        if st.button("Generate analysis"):
            prompt = f"""
Kamu adalah analis B2B dari Telkomsel Enterprise. Berdasarkan pendekatan R3C4P, khususnya pilar pertama: PROFILE,
buatlah output analisa naratif dan tabel Profil Perusahaan (Tabel 1.1) untuk:

Nama Perusahaan: {customer_name}
Level Analisa: {level}

Tampilkan output sebagai:
1. Narasi problem statement (mengikuti format R3C4P):
- Masalah yang kami hadapi adalah: ...
- Hal ini disebabkan oleh: ...
- Ini menyebabkan beberapa masalah seperti: ...
- Terutama bagi: ...
- Jika masalah ini berlanjut, maka akan terjadi: ...
- Bahkan saat ini, masalah ini sudah menghambat kami untuk: ...

2. Tabel profil perusahaan (Tabel 1.1) dengan elemen:
- Nama Perusahaan
- Industri
- Holding
- Lokasi Kantor Pusat
- Jumlah Cabang/Kantor
- Jumlah Karyawan
- Jumlah Pelanggan
- Revenue (Rupiah)
- Jumlah Aset (Rupiah)
- Struktur Permodalan
- Customer (B2B, B2G)
- Mitra/Suplier
- Produk Utama (Merk)
- Website/Email/Telp
- Status Digitalisasi

Tuliskan dalam bahasa Indonesia dengan gaya profesional.
"""
            try:
                try:
                    response = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[{"role": "user", "content": prompt}]
                    )
                except openai.RateLimitError:
                    st.warning("❗ GPT-4o limit reached, switching to GPT-3.5...")
                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[{"role": "user", "content": prompt}]
                    )

                output = response.choices[0].message.content
                st.markdown("### 🔍 GPT R3C4P Profile Analysis")
                st.markdown(output)

            except Exception as e:
                st.error(f"Gagal memanggil OpenAI API: {e}")

    elif st.session_state.page == "Map pain points":
        st.write("Identify key issues and map to Telkomsel solutions.")

    elif st.session_state.page == "Construct business model":
        st.write("Use BMC and USP logic to define business initiatives.")

    elif st.session_state.page == "Retrieve insights":
        st.write("Access trends, competitor strategy, and industry updates.")

elif authentication_status is False:
    st.error("Invalid username or password")
elif authentication_status is None:
    st.warning("Please enter your credentials")
