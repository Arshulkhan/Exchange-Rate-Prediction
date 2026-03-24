import pandas as pd
import os

USER_DB = "data/users.csv"


def load_users():
    if not os.path.exists(USER_DB):
        df = pd.DataFrame(columns=["username", "email", "password", "created_at"])
        df.to_csv(USER_DB, index=False)

    try:
        df = pd.read_csv(USER_DB)
    except pd.errors.EmptyDataError:
        df = pd.DataFrame(columns=["username", "email", "password", "created_at"])

    credentials = {"usernames": {}}

    for _, row in df.iterrows():
        credentials["usernames"][row["username"]] = {
            "email": row["email"],
            "name": row["username"],
            "password": row["password"]
        }

    return credentials
