
import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Hugging Face API info
HF_API_URL = "https://api-inference.huggingface.co/models/ByteDance/SDXL-Lightning"
HF_HEADERS = {"Authorization": f"Bearer {st.secrets['HF_API_KEY']}"}

st.set_page_config(page_title="StyleMind AI", layout="centered")
st.title("👕 StyleMind AI – Outfit Generator with Images")
st.write("Generate stylish outfit visuals using Hugging Face's SDXL-Lightning.")

# --- User Input Form ---
with st.form("style_form"):
    occasion = st.selectbox("What is the occasion?", [
        "Date Night", "Office Meeting", "Beach Day", "Wedding Guest", "Travel", "Casual Outing", "Party", "Brunch"])
    gender = st.selectbox("Gender", ["Male", "Female", "Unisex"])
    season = st.selectbox("Season", ["Summer", "Winter", "Spring", "Autumn"])
    style = st.selectbox("Style Type", [
        "Casual", "Formal", "Streetwear", "Business Casual", "Beachwear", "Smart Casual"])
    submitted = st.form_submit_button("Generate Outfit Image")

if submitted:
    prompt = f"Flat lay of a {style.lower()} {season.lower()} outfit for a {gender.lower()} attending a {occasion.lower()}. Include top, bottom, shoes, and accessories. Displayed on a clean background."

    with st.spinner("Generating outfit image with SDXL-Lightning..."):
        try:
            response = requests.post(
                HF_API_URL,
                headers=HF_HEADERS,
                json={"inputs": prompt}
            )

            if response.status_code == 200:
                image = Image.open(BytesIO(response.content))
                st.success("Here is your outfit suggestion!")
                st.image(image, caption="Outfit Suggestion", use_column_width=True)
            else:
                st.error(f"API Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"Error generating image: {e}")
