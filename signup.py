import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
from datetime import datetime
import os

USER_DB = "data/users.csv"


def signup_form():
    st.title("📝 Create Account")

    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm = st.text_input("Confirm Password", type="password")

    if st.button("Sign Up"):

        if not username or not email or not password:
            st.error("All fields are required")
            return

        if password != confirm:
            st.error("Passwords do not match")
            return

        # Create file if not exists
        if not os.path.exists(USER_DB):
            df = pd.DataFrame(columns=["username", "email", "password", "created_at"])
            df.to_csv(USER_DB, index=False)

        # Load safely
        try:
            df = pd.read_csv(USER_DB)
        except pd.errors.EmptyDataError:
            df = pd.DataFrame(columns=["username", "email", "password", "created_at"])

        if username in df.get("username", []):
            st.error("Username already exists")
            return

        hashed = stauth.Hasher([password]).generate()[0]

        new_user = {
            "username": username,
            "email": email,
            "password": hashed,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        df = pd.concat([df, pd.DataFrame([new_user])], ignore_index=True)
        df.to_csv(USER_DB, index=False)

        st.success("✅ Account created successfully! You can now login.")
