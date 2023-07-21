# Import os to set API key
import os
import requests
import io
from PIL import Image

from dotenv import find_dotenv,load_dotenv
# Bring in streamlit for UI/app interface
import streamlit as st
import requests




load_dotenv(find_dotenv())

#Set HF API TOKEN
HUGGINGFACEHUB_API_TOKEN=os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Create instance of HF GP2 LLM

API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": f"Bearer {HUGGINGFACEHUB_API_TOKEN}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

# You can access the image with PIL.Image for example


st.title('🦜🔗 BHZ Image Generator')
# Create a text input box for the user
prompt = st.text_input('Input your prompt here')
	

# If the user hits enter
if prompt:
    # Then pass the prompt to the LLM
    response = query(prompt)
    image = Image.open(io.BytesIO(response))
    #response = agent_executor.run(prompt)
    # ...and write it out to the screen
    st.image(image)
