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
        f"A fashion visual featuring a {gender.lower()} outfit for a {occasion.lower()} in {season.lower()}. "
        f"The style is {style.lower()}.\n\n"
        f"Scene 1: A Pinterest-style flat lay arranged on a soft beige or off-white background. Includes styled topwear "
        f"(e.g., shirt or blouse), bottomwear (e.g., chinos, skirt), matching footwear (e.g., loafers, sneakers), and 1–2 accessories "
        f"(watch, sunglasses, bracelet, handbag). Subtle shadows and neutral lighting for a modern aesthetic.\n\n"
        f"Scene 2: A mannequin wearing the same outfit, posed naturally in front of a simple light-colored background. "
        f"Include visible fabric textures, folds, and accurate color coordination. The focus should be on clean presentation "
        f"with a minimalistic editorial look. Use soft shadows and centered framing."
    )

    if custom_notes.strip():
        prompt += f"\n\nAdditional styling notes: {custom_notes.strip()}"

    st.success("Here is your styled outfit prompt:")
    st.code(prompt, language="text")
