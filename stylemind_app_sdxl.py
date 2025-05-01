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
        f"A styled fashion concept featuring a {gender.lower()} outfit designed for a {occasion.lower()} during the {season.lower()} season. "
        f"The fashion aesthetic is {style.lower()}, aligned with seasonal trends and color harmony.

"

        f"Scene 1: A Pinterest-style flat lay arranged on a soft beige or light gray background. Include clearly labeled pieces:
"
        f"- Topwear: lightweight linen or breathable cotton shirt,
"
        f"- Bottomwear: linen trousers or chino shorts,
"
        f"- Footwear: canvas sneakers or leather sandals,
"
        f"- Accessories: a stainless steel watch, fabric tote bag, and acetate-frame sunglasses.
"
        f"Use soft directional lighting and natural shadows. Colors should reflect the season (e.g., earthy tones for autumn, brights for summer).

"

        f"Scene 2: A mannequin fully dressed in the same outfit — including all accessories and layering pieces like scarves, hats, or outerwear where appropriate. "
        f"The mannequin should be standing in a clean studio setting with neutral lighting. Clearly show textures (linen, cotton, denim, wool), stitching detail, and natural fabric drape. "
        f"Use high-fashion catalog-style framing with soft shadows and light bounce."
    )} outfit for a {gender.lower()} attending a {occasion.lower()} in {season.lower()}. "
        f"Include a linen or cotton shirt, chino pants or denim jeans, loafers or sneakers, and 1–2 accessories such as sunglasses or a watch. "
        f"Display all items arranged neatly on a clean white or beige background."
    )

    if reference != "None":
        prompt += f"

Visual inspiration is drawn from {reference.lower()}, known for its influence on current fashion trends and editorial aesthetics."

    if custom.strip():
        prompt += f"

Additional styling notes: {custom.strip()}":
        prompt += f" Additional styling notes: {custom.strip()}"

    st.success("Here is your outfit prompt:")
    st.code(prompt, language="text")
