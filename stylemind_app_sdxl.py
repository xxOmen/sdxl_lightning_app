# Streamlit App – StyleMind Outfit Prompt Generator (Text Only)

import streamlit as st

st.set_page_config(page_title="StyleMind Prompt Generator", layout="wide")
st.title("📝 StyleMind AI – Outfit Prompt Generator")
st.write("Generate rich, styled fashion prompts for use in AI tools like DALL·E, Midjourney, or for design moodboards.")

# --- User Input Form ---
with st.form("prompt_form"):
    occasion = st.selectbox("What is the occasion?", [
        "Date Night", "Office Meeting", "Beach Day", "Wedding Guest", "Travel", "Casual Outing", "Party", "Brunch"])
    gender = st.selectbox("Gender", ["Male", "Female", "Unisex"])
    season = st.selectbox("Season", ["Summer", "Winter", "Spring", "Autumn"])
    style = st.selectbox("Style Type", [
        "Casual", "Formal", "Streetwear", "Business Casual", "Beachwear", "Smart Casual"])
    reference = st.selectbox("Fashion Inspiration Reference:", [
        "None", "Outfits from Euphoria characters", "Timothée Chalamet street style", "Gigi Hadid off-duty looks", 
        "Old Money aesthetic from TikTok", "Pinterest flat lays", "Zara catalog 2024", "Uniqlo minimalist ads", 
        "Instagram fashion influencers", "Emily in Paris aesthetic", "Met Gala celebrity themes"])
    custom = st.text_area("Custom Notes (optional)", placeholder="e.g. include an oversized blazer or earthy tones")
    submitted = st.form_submit_button("Generate Outfit Prompt")

if submitted:
    prompt = (
        f"A flat lay of a {style.lower()} outfit for a {gender.lower()} attending a {occasion.lower()} in {season.lower()}. "
        f"Include a linen or cotton shirt, chino pants or denim jeans, loafers or sneakers, and 1–2 accessories such as sunglasses or a watch. "
        f"Display all items arranged neatly on a clean white or beige background."
    )

    if reference != "None":
        prompt += (
            f" The overall outfit style and visual layout should be inspired by {reference.lower()}, "
            f"reflecting current fashion trends, seasonal color palettes, and editorial styling used by celebrities, influencers, and fashion magazines. "
            f"Include modern layering, seasonal materials, and trending styling choices often seen in designer campaigns or pop culture looks."
        )

    if custom.strip():
        prompt += f" Additional styling notes: {custom.strip()}"

    st.success("Here is your outfit prompt:")
    st.code(prompt, language="text")
