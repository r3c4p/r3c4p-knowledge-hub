
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

    # Sidebar left
    with st.sidebar:
        st.markdown("### R3C4P Knowledge Hub")
        st.markdown("Hello! How can I assist you today?")
        selected = st.radio("Navigation", [
            "Identify a customer",
            "Map pain points",
            "Construct business model",
            "Retrieve insights"
        ])

    # Layout columns
    col_sidebar, col_main, col_right = st.columns([1, 3, 1])

    with col_main:
        if selected == "Identify a customer":
            st.header("Identify a customer")
            st.write("I can analyze a customer based on the 4P (Profile, People, Process, Problem) R3C4P framework.")
            customer_name = st.text_input("Customer name", "PT Industri Jaya Komponen")
            level = st.selectbox("Analysis level", ["Corporate Group", "Corporate", "Division", "Project", "Subsidiary"])
            if st.button("Generate analysis"):
                st.markdown("### Customer Profile, People, Process, Problem")
                with st.expander("▶ Profile"):
                    st.write("Customer identity and structure")
                with st.expander("▶ People"):
                    st.write("Key customer personnel")
                with st.expander("▶ Process"):
                    st.write("Workflows or current business process")
                with st.expander("▶ Problem"):
                    st.write("Identified pain points or gaps")

        elif selected == "Map pain points":
            st.header("Map out pain points")
            st.write("Help identify key issues and recommend suitable Telkomsel solutions.")
        elif selected == "Construct business model":
            st.header("Construct a business model")
            st.write("Use BMC and USP logic to define business initiative.")
        elif selected == "Retrieve insights":
            st.header("Retrieve industry-specific updates")
            st.write("Access trends, competitor strategy, and related industry news.")

    with col_right:
        st.markdown("### 4P Analytic Levels")
        st.markdown("- Corporate Group\n- Corporate\n- Division\n- Project\n- Subsidiary")
        st.markdown("### R3C4P Framework")
        st.markdown("• **Profile**: customer identity and status\n"
                    "• **People**: key roles and organization\n"
                    "• **Process**: workflows or existing solutions\n"
                    "• **Problem**: underlying needs or pain points")

elif authentication_status is False:
    st.error("Invalid username or password")
elif authentication_status is None:
    st.warning("Please enter your credentials")
