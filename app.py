import os
import requests
import streamlit as st
import streamlit.components.v1 as components
from dotenv import load_dotenv

# load Brewit API key from .env file
load_dotenv()
BREWIT_API_KEY = os.getenv("BREWIT_API_KEY")

brewit_url = "https://api.brewit.ai/v1/auth/signin_external"


def generate_jwt():
    # construct a user payload
    payload = {
        "external_id": "1",  # TODO: replace with your user's unique identifier
        "ttl_seconds": 3600,
        "display_name": "",  # TODO: (optional) replace with your user's display name
        "email": "",  # TODO: (optional) replace with your user's email
        "picture": "",  # TODO: (optional) replace with your user's profile picture
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": BREWIT_API_KEY,
    }

    response = requests.request("POST", brewit_url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()["token"]
    return None


# Generate a JWT token
jwt = generate_jwt()

# Construct the Brewit chat agent embed URL
embed_url = f"https://app.brewit.ai/embed/chat?workspace_id=3697a93c-daa4-4068-ad42-164a1b149710&resource_id=2c38be6d-2199-4297-a653-1053e2c9e5b6&jwt={jwt}"

st.set_page_config(layout="wide")
st.title("Brewit Embedded Chat Agent")

# Embed the Brewit chat agent using an iframe
components.iframe(embed_url, height=800, width=1300, scrolling=True)
