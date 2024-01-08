import streamlit as st
st.set_page_config(layout='wide')
st.write('Login')

def login():
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Simulate a simple login check (replace this with actual authentication logic)
        if username == "VIKABH" and password == "VKB@321":
            st.success("Login successful!")
            # Redirect to another page after successful login
            st.markdown(
                """
                <meta http-equiv="refresh" content="2;URL='http://localhost:8503/'"/>
                """
                , unsafe_allow_html=True
            )
        else:
            st.error("Invalid credentials. Please try again.")

login()






