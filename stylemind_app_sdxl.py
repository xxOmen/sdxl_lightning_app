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

# --- Season-based Material Mapping ---
material_top = {
    "Summer": "lightweight linen or breathable cotton shirt",
    "Winter": "wool sweater or knit turtleneck",
    "Spring": "cotton blouse or layered chambray shirt",
    "Autumn": "corduroy shirt or flannel button-up",
    "All Seasons": "versatile cotton or lightweight knit shirt"
}

material_bottom = {
    "Summer": "linen trousers or chino shorts",
    "Winter": "wool pants or thick denim jeans",
    "Spring": "cotton chinos or pleated culottes",
    "Autumn": "corduroy trousers or wool skirt",
    "All Seasons": "neutral denim jeans or versatile trousers"
}

material_footwear = {
    "Summer": "canvas sneakers or leather sandals",
    "Winter": "leather boots or suede loafers",
    "Spring": "white sneakers or lace-up oxfords",
    "Autumn": "ankle boots or loafers",
    "All Seasons": "clean sneakers or brogues"
}

# --- Generate Prompt ---
if submitted:
    top = material_top[season]
    bottom = material_bottom[season]
    shoes = material_footwear[season]

    prompt = (
        f"A styled fashion concept featuring a {gender.lower()} outfit designed for a {occasion.lower()} during the {season.lower()} season. "
        f"The fashion aesthetic is {style.lower()}, aligned with seasonal trends and color harmony.\n\n"

        f"Scene 1: A Pinterest-style flat lay arranged on a soft beige or light gray background. Include clearly labeled pieces:\n"
        f"- Topwear: {top},\n"
        f"- Bottomwear: {bottom},\n"
        f"- Footwear: {shoes},\n"
        f"- Accessories: a stainless steel watch, fabric tote bag, and acetate-frame sunglasses.\n"
        f"Use soft directional lighting and natural shadows. Colors should reflect the season (e.g., earthy tones for autumn, brights for summer).\n\n"

        f"Scene 2: A mannequin fully dressed in the same outfit — including all accessories and layering pieces like scarves, hats, or outerwear where appropriate. "
        f"The mannequin should be standing in a clean studio setting with neutral lighting. Clearly show textures (linen, cotton, denim, wool), stitching detail, and natural fabric drape. "
        f"Use high-fashion catalog-style framing with soft shadows and light bounce."
    )

    if custom_notes.strip():
        prompt += f"\n\nAdditional styling notes: {custom_notes.strip()}"

    st.success("Here is your styled outfit prompt:")
    st.code(prompt, language="text")
