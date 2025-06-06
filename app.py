
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
            st.markdown("### Customer Profile, People, Process, Problem")
            with st.expander("▶ Profile"):
                st.write("Customer identity and structure")
            with st.expander("▶ People"):
                st.write("Key customer personnel")
            with st.expander("▶ Process"):
                st.write("Workflows or current business process")
            with st.expander("▶ Problem"):
                st.write("Identified pain points or gaps")

    elif st.session_state.page == "Map pain points":
        st.write("Identify key issues and map to Telkomsel solutions.")
    elif st.session_state.page == "Construct business model":
        st.write("Use BMC and USP logic to define business initiatives.")
    elif st.session_state.page == "Retrieve insights":
        st.write("Access trends, competitor strategy, and industry updates.")

    # Reference section
    st.markdown("---")
    st.subheader("4P Analytic Levels")
    st.markdown("- Corporate Group  
- Corporate  
- Division  
- Project  
- Subsidiary")

    st.subheader("R3C4P Framework")
    st.markdown("**Profile**: customer identity and status  
"
                "**People**: key roles and organization  
"
                "**Process**: workflows or existing solutions  
"
                "**Problem**: underlying needs or pain points")

elif authentication_status is False:
    st.error("Invalid username or password")
elif authentication_status is None:
    st.warning("Please enter your credentials")
