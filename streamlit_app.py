import streamlit as st
import requests

# Tavus API key
API_KEY = "461e847e076d4c72810631d97cc09fa1"
BASE_URL = "https://api.tavus.io/v1"  # Update this URL to the correct Tavus API endpoint if needed.

st.title("Persona Video Conversation")

# Sidebar for settings
st.sidebar.header("Settings")
persona_name = st.sidebar.text_input("Persona Name", "Default Persona")
script = st.sidebar.text_area(
    "Enter Script",
    "Hello! I’m excited to share more about our persona video capabilities."
)

# Upload a video if needed (optional)
uploaded_file = st.sidebar.file_uploader("Upload Background Video (optional)", type=["mp4"])

# Function to call Tavus API
def create_video(api_key, name, script, video_file=None):
    headers = {"Authorization": f"Bearer {api_key}"}
    data = {"name": name, "script": script}
    files = {}

    if video_file:
        files["background_video"] = video_file

    response = requests.post(
        f"{BASE_URL}/videos",
        headers=headers,
        data=data,
        files=files
    )

    if response.status_code == 201:
        return response.json().get("video_url")
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
        return None

# Create video on button click
if st.button("Generate Video"):
    with st.spinner("Generating video..."):
        video_url = create_video(API_KEY, persona_name, script, uploaded_file)

        if video_url:
            st.success("Video generated successfully!")
            st.video(video_url)

# Option to preview video
st.write("Preview the generated video below.")
