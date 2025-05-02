import streamlit as st

st.set_page_config(page_title="StyleMind Prompt Generator", layout="wide")
st.title("📝 StyleMind AI – Outfit Prompt Generator")
st.write("Elevate your fashion game with your personal AI stylist, creating curated fashion prompts that bring your style vision to life")

# --- User Input Form ---
with st.form("prompt_form"):
    occasion = st.selectbox("What is the occasion?", [
        "Date Night", "Office Meeting", "Beach Day", "Wedding Guest", "Travel", "Casual Outing", "Party", "Brunch"],
        help="Select the occasion for which the outfit is being generated.")
    
    gender = st.selectbox("Gender", ["Male", "Female", "Unisex"], help="Choose the gender for the outfit.")
    
    season = st.selectbox("Season", ["Summer", "Winter", "Spring", "Autumn"], help="Choose the season to match the outfit.")
    
    style = st.selectbox("Style Type", [
        "Casual", "Formal", "Streetwear", "Business Casual", "Beachwear", "Smart Casual"], 
        help="Select the style type of the outfit.")
    
    reference = st.selectbox("Fashion Inspiration Reference:", [
        "None", "Outfits from Euphoria characters", "Timothée Chalamet street style", "Gigi Hadid off-duty looks", 
        "Old Money aesthetic from TikTok", "Pinterest flat lays", "Zara catalog 2024", "Uniqlo minimalist ads", 
        "Instagram fashion influencers", "Emily in Paris aesthetic", "Met Gala celebrity themes"],
        help="Select a fashion inspiration reference, if any.")
    
    custom = st.text_area("Custom Notes (optional)", placeholder="e.g. include an oversized blazer or earthy tones",
                          help="Add any specific styling preferences here.")
    
    submitted = st.form_submit_button("Generate Outfit Prompt")

# --- Processing Form Submission ---
if submitted:
    if not (occasion and gender and season and style):  # Simple validation
        st.warning("Please make sure all fields are selected.")
    else:
        # Define the prompt template with grid-based layout for items
        prompt = (
            f"**Outfit Grid Generator** for a {gender.lower()} designed for a {occasion.lower()} in the {season.lower()} season. "
            f"The fashion aesthetic is {style.lower()}, aligned with seasonal trends and color harmony.\n\n"

            f"Generate a grid of outfits, each with clearly defined clothing items and accessories. Include outfits with multiple combinations of shirts, jackets, pants, footwear, and accessories in each row, and ensure color harmony across items.\n\n"
        )

        # Scene 1: Grid-based layout
        prompt += (
            f"Scene 1: A Pinterest-style grid display with multiple outfits. Each outfit features distinct clothing items with clear color palettes. "
            f"Example 1: Beige linen shirt, olive green chinos, white sneakers, and simple accessories like a watch and sunglasses. "
            f"Example 2: Dark grey wool sweater, navy denim pants, leather boots, scarf. Each outfit should be laid out with attention to textures and color balance.\n\n"
        )

        # Scene 2: Full outfit on a mannequin
        prompt += (
            f"Scene 2: A mannequin fully dressed in each complete outfit from Scene 1. Ensure the mannequin's pose shows off the full outfit clearly, "
            f"with close-up shots that highlight fabric textures, colors, and details like stitching and folds.\n\n"
        )

        if reference != "None":
            prompt += f"\n\nVisual inspiration is drawn from {reference.lower()}, known for its influence on fashion culture and contemporary styling."

        if custom.strip():
            prompt += f"\n\nAdditional styling notes: {custom.strip()}"

        st.success("Here is your outfit prompt:")
        st.markdown("### Fashion Prompt")
        st.code(prompt, language="text")
