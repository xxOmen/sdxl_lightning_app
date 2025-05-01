# Streamlit App for StyleMind AI – Image with Labels Display

import streamlit as st
import openai

# Load OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="StyleMind AI", layout="wide")
st.title("👕 StyleMind AI – Outfit Generator with Labels")
st.write("Generate stylish outfit visuals using DALL·E 3 and show item labels alongside.")

# --- User Input Form ---
with st.form("style_form"):
    occasion = st.selectbox("What is the occasion?", [
        "Date Night", "Office Meeting", "Beach Day", "Wedding Guest", "Travel", "Casual Outing", "Party", "Brunch"])
    gender = st.selectbox("Gender", ["Male", "Female", "Unisex"])
    season = st.selectbox("Season", ["Summer", "Winter", "Spring", "Autumn"])
    style = st.selectbox("Style Type", [
        "Casual", "Formal", "Streetwear", "Business Casual", "Beachwear", "Smart Casual"])
    submitted = st.form_submit_button("Generate Outfit Images")

if submitted:
    prompt = f"A flat lay of a {style.lower()} outfit for a {gender.lower()} attending a {occasion.lower()} in {season.lower()}. Include a linen or cotton shirt, chino pants or denim jeans, loafers or sneakers, and 1–2 accessories such as sunglasses or a watch. Display all items arranged neatly on a clean white or beige background."

    image_urls = []
    with st.spinner("Generating 4 outfit images with DALL·E 3..."):
        for _ in range(4):
            try:
                response = openai.images.generate(
                    model="dall-e-3",
                    prompt=prompt,
                    size="1024x1024",
                    quality="standard",
                    n=1
                )
                image_urls.append(response.data[0].url)
            except Exception as e:
                st.error(f"Error generating image: {e}")

    if image_urls:
        st.success("Here are your outfit suggestions with labeled items!")
        labels = [
            ["Linen shirt", "Chino trousers", "Leather loafers", "Stainless steel watch", "Sunglasses"],
            ["Cotton t-shirt", "Denim jeans", "Canvas sneakers", "Canvas tote bag", "Watch"],
            ["Flannel overshirt", "Corduroy pants", "Suede boots", "Wool scarf", "Leather strap watch"],
            ["Button-down shirt", "Slim chinos", "Sneakers", "Messenger bag", "Wayfarer sunglasses"]
        ]

        for i, url in enumerate(image_urls):
            cols = st.columns([2, 1])
            with cols[0]:
                st.image(url, caption=f"Outfit Suggestion {i+1}", use_column_width=True)
            with cols[1]:
                st.markdown("**Items Included:**")
                for item in labels[i]:
                    st.markdown(f"- {item}")
    else:
        st.warning("No images were generated. Please try again.")
