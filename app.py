import streamlit as st
import streamlit_authenticator as stauth
import yaml
import pandas as pd
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

    st.sidebar.markdown("### R3C4P Knowledge Hub")
    st.sidebar.markdown("Hello! How can I assist you today?")

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
        st.write("Analyze a customer based on the 4P R3C4P framework.")
        customer_name = st.text_input("Customer name", "PT Industri Jaya Komponen")
        level = st.selectbox("Analysis level", ["Corporate Group", "Corporate", "Division", "Project", "Subsidiary"])

        if st.button("Generate analysis"):
            with st.form("profil_form"):
                st.subheader("1.1 Company Profile")
                nama_perusahaan = st.text_input("Nama Perusahaan")
                industri = st.text_input("Industri")
                holding = st.text_input("Holding")
                lokasi = st.text_input("Lokasi Kantor Pusat")
                jumlah_cabang = st.number_input("Jumlah Cabang/Kantor", min_value=0)
                jumlah_karyawan = st.number_input("Jumlah Karyawan", min_value=0)
                jumlah_pelanggan = st.number_input("Jumlah Pelanggan", min_value=0)
                revenue = st.text_input("Revenue (Rupiah)")
                jumlah_aset = st.text_input("Jumlah Aset (Rupiah)")
                struktur_permodalan = st.text_input("Struktur Permodalan")
                customer_type = st.selectbox("Customer", ["B2B", "B2G", "Keduanya"])
                mitra = st.text_input("Mitra/Suplier")
                produk_utama = st.text_input("Produk Utama (Merk)")
                kontak = st.text_input("Website/Email/Telp")
                status_digital = st.selectbox("Status Digitalisasi", ["Digital Ready", "Digitalizing", "Konvensional"])

                submitted = st.form_submit_button("Simpan dan Tampilkan")
                if submitted:
                    st.session_state["profil_perusahaan"] = {
                        "Nama Perusahaan": nama_perusahaan,
                        "Industri": industri,
                        "Holding": holding,
                        "Lokasi Kantor Pusat": lokasi,
                        "Jumlah Cabang/Kantor": jumlah_cabang,
                        "Jumlah Karyawan": jumlah_karyawan,
                        "Jumlah Pelanggan": jumlah_pelanggan,
                        "Revenue (Rupiah)": revenue,
                        "Jumlah Aset (Rupiah)": jumlah_aset,
                        "Struktur Permodalan": struktur_permodalan,
                        "Customer (B2B, B2G)": customer_type,
                        "Mitra/Suplier": mitra,
                        "Produk Utama (Merk)": produk_utama,
                        "Website/Email/Telp": kontak,
                        "Status Digitalisasi": status_digital
                    }

            if "profil_perusahaan" in st.session_state:
                st.markdown("### Output Tabel 1.1 - Profil Perusahaan")
                profil_dict = st.session_state["profil_perusahaan"]
                profil_df = pd.DataFrame({
                    "Elemen Profil": list(profil_dict.keys()),
                    "Data": list(profil_dict.values())
                })
                st.table(profil_df)

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
