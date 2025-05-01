import streamlit as st

st.set_page_config(page_title="StyleMind Prompt Generator", layout="centered")
st.title("📝 StyleMind AI – Advanced Outfit Prompt Generator")
st.write("Generate rich, styled outfit prompts for DALL·E, Midjourney, or any AI tool.")

# --- User Input Form ---
with st.form("prompt_form"):
    occasion = st.selectbox("What is the occasion?", [
        "Date Night", "Office Meeting", "Beach Day", "Wedding Guest", "Travel", "Casual Outing",
        "Party", "Brunch", "Outdoor Hike", "Festival", "Dinner with Friends", "Work From Home"])
    gender = st.selectbox("Gender", ["Male", "Female", "Unisex", "Non-Binary", "Other"])
    season = st.selectbox("Season", ["Summer", "Winter", "Spring", "Autumn", "All Seasons"])
    style = st.selectbox("Style Type", [
        "Casual", "Formal", "Streetwear", "Business Casual", "Beachwear", "Smart Casual",
        "Athleisure", "Boho", "Preppy", "Minimalist", "Techwear"])
    custom_notes = st.text_area("Additional description (optional)", placeholder="e.g. include a leather belt or floral print")
    submitted = st.form_submit_button("Generate Prompt")

# --- Generate Prompt ---
if submitted:
    prompt = (
        f"A styled fashion concept featuring a {gender.lower()} outfit designed for a {occasion.lower()} during the {season.lower()} season. "
        f"The fashion aesthetic is {style.lower()}, inspired by current trends and season-appropriate colors.\n\n"

        f"Scene 1: A Pinterest-style flat lay arrangement on a soft beige, stone gray, or off-white background. Include:\n"
        f"- Topwear labeled by material and type (e.g., 'cotton t-shirt', 'linen blouse'),\n"
        f"- Bottomwear (e.g., 'denim jeans', 'pleated wool skirt'),\n"
        f"- Footwear (e.g., 'white leather sneakers', 'suede loafers'),\n"
        f"- 2–3 accessories (e.g., 'canvas tote bag', 'stainless steel watch', 'acetate sunglasses').\n"
        f"Ensure shadows are soft and item spacing is clean. Colors should reflect the chosen season and style (e.g., earthy for autumn, pastel for spring).\n\n"

        f"Scene 2: A mannequin or model wearing the full coordinated outfit, including all core pieces and accessories — such as jacket, hat, socks, bag, and jewelry if suitable. "
        f"Outfit should be worn naturally and posed in a minimalist studio setting. Emphasize realistic textures (cotton, wool, leather, denim), fabric folds, and light reflection. "
        f"Use fashion catalog-style composition with centered framing and soft lighting."
    )

    if custom_notes.strip():
        prompt += f"\n\nAdditional styling notes: {custom_notes.strip()}"

    st.success("Here is your styled outfit prompt:")
    st.code(prompt, language="text")
